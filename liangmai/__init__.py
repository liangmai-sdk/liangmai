"""
量脉 (Liangmai) 金融数据平台 Python SDK。

用法::

    from liangmai import Client

    client = Client(token="your_liangmai_token")

    # 股票列表
    data = client.stock_list()

    # 实时行情
    data = client.stock_realtime(ts_code="601012")

    # 涨停股池
    data = client.pool_limit_up(trade_date="2025-04-01")

也可以直接调用底层网关函数::

    from liangmai import call

    data = call("stock_realtime", ts_code="601012", token="your_token")

设置环境变量可免去每次传 token::

    export LIANGMAI_TOKEN=your_token
    export LIANGMAI_BASE_URL=https://liangmai.pro/api/gateway  # 可选，默认值
"""

from .client import Client, call, API_COUNT
from .gateway import call_gateway

__all__ = ["Client", "call", "call_gateway", "API_COUNT"]
__version__ = "0.2.1"
