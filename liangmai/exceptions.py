"""量脉 SDK 自定义异常。"""


class LiangmaiError(Exception):
    """SDK 基础异常。"""

    pass


class AuthenticationError(LiangmaiError):
    """Token 无效或鉴权失败（HTTP 401/403）。"""

    pass


class RateLimitError(LiangmaiError):
    """请求频率超限（HTTP 429）。"""

    pass


class ApiError(LiangmaiError):
    """API 业务错误（code != 0 且非 5xx）。

    属性
    ----
    code : int
        平台返回的 code。
    msg : str
        平台返回的错误信息。
    """

    def __init__(self, code: int, msg: str) -> None:
        self.code = code
        self.msg = msg
        super().__init__(f"API 错误 code={code}: {msg}")