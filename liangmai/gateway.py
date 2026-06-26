"""
量脉网关底层请求模块。

调用 /api/gateway，对齐文档页 `fetchGatewayWithRetry` 的重试与错误处理约定。
"""

import json
import os
import time
from typing import Any, Dict, Optional

import requests

DEFAULT_BASE_URL = os.environ.get("LIANGMAI_BASE_URL", "https://liangmai.pro/api/gateway").rstrip("/")
DEFAULT_TOKEN = os.environ.get("LIANGMAI_TOKEN", "")


def _should_retry_like_docs(status_code: int, payload: Dict[str, Any]) -> bool:
    """与 /docs 内 fetchGatewayWithRetry 一致：5xx 或 JSON code=500 时重试一次。"""
    if 500 <= status_code <= 504:
        return True
    try:
        return int(payload.get("code", 0)) == 500
    except (TypeError, ValueError):
        return False


def call_gateway(
    api: str,
    token: Optional[str] = None,
    base_url: Optional[str] = None,
    timeout: float = 30,
    retry_once: bool = True,
    **params: Any,
) -> Dict[str, Any]:
    """GET 调用量脉网关，自动附加 token；业务参数放在 kwargs。

    参数
    ----
    api : str
        接口别名，例如 ``"stock_realtime"``、``"pool_limit_up"``。
    token : str, optional
        平台发放的 Token；未传时从环境变量 ``LIANGMAI_TOKEN`` 读取。
    base_url : str, optional
        网关地址；未传时从环境变量 ``LIANGMAI_BASE_URL`` 读取，
        默认 ``https://liangmai.pro/api/gateway``。
    timeout : float
        请求超时秒数，默认 30。
    retry_once : bool
        是否在首次 5xx 或 code=500 时自动重试一次，默认 True。
    **params
        业务参数（如 ts_code、trade_date、interval 等）。

    返回
    ----
    dict
        平台 JSON 响应体，正常时 ``code`` 为 0。
    """
    _token: str = token if token else DEFAULT_TOKEN
    _base_url: str = (base_url if base_url else DEFAULT_BASE_URL).rstrip("/")

    if not _token:
        raise RuntimeError("请设置环境变量 LIANGMAI_TOKEN 或传入 token 参数")

    q: Dict[str, Any] = {"token": _token, "api": api}
    for k, v in params.items():
        if v is None or k in ("retry_once",):
            continue
        q[k] = v

    for attempt in range(2 if retry_once else 1):
        r = requests.get(_base_url, params=q, timeout=timeout)
        try:
            data: Dict[str, Any] = r.json()
        except json.JSONDecodeError:
            raise RuntimeError("非 JSON 响应 HTTP {}: {}".format(r.status_code, r.text[:500])) from None

        if data.get("code") == 0:
            return data

        if attempt == 0 and retry_once and _should_retry_like_docs(r.status_code, data):
            time.sleep(0.4)
            continue

        raise RuntimeError(
            "业务失败 HTTP {} code={} msg={} meta={}".format(
                r.status_code, data.get("code"), data.get("msg"), data.get("meta")
            )
        )

    raise RuntimeError("网关请求失败")