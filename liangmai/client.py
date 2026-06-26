"""
量脉 Python SDK 客户端。

提供平台全部 105 个数据接口的便捷方法，封装网关调用。
"""

from typing import Any, Dict, Optional

from .gateway import call_gateway

# 平台接口总数
API_COUNT = 105


class Client:
    """量脉数据平台 Python 客户端 — 封装全部 105 个接口。

    用法::

        from liangmai import Client

        client = Client(token="your_token")
        data = client.stock_list()

    参数
    ----
    token : str, optional
        平台发放的 Token；未传时从环境变量 ``LIANGMAI_TOKEN`` 读取。
    base_url : str, optional
        网关地址；未传时从环境变量 ``LIANGMAI_BASE_URL`` 读取，
        默认 ``https://liangmai.pro/api/gateway``。
    timeout : float
        请求超时秒数，默认 30。
    """

    def __init__(
        self,
        token=None,  # type: Optional[str]
        base_url=None,  # type: Optional[str]
        timeout=30,  # type: float
    ):
        # type: (...) -> None
        self._token = token
        self._base_url = base_url
        self._timeout = timeout

    def _call(self, api, **params):
        # type: (str, **Any) -> Dict[str, Any]
        return call_gateway(
            api=api,
            token=self._token,
            base_url=self._base_url,
            timeout=self._timeout,
            **params,
        )

    def _stock_code_params(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        if ts_code:
            return {"ts_code": ts_code}
        elif code:
            return {"code": code}
        elif symbol:
            return {"symbol": symbol}
        raise ValueError("请传入 ts_code、code 或 symbol")

    # ========================================================================
    # 列表与日历 (13)
    # ========================================================================

    def stock_list(self):
        # type: () -> Dict[str, Any]
        """沪深京股票合并列表（平台聚合，推荐）。"""
        return self._call("stock_list")

    def hs_list_main(self):
        # type: () -> Dict[str, Any]
        """沪深 A 股基础列表（不含北证合并）。"""
        return self._call("hs_list_main")

    def ipo_calendar(self):
        # type: () -> Dict[str, Any]
        """新股日历（按申购日期倒序）。"""
        return self._call("ipo_calendar")

    def sector_tree(self):
        # type: () -> Dict[str, Any]
        """指数/行业/概念树。"""
        return self._call("sector_tree")

    def sector_constituents(self, sector_code):
        # type: (str) -> Dict[str, Any]
        """按板块/概念代码查成分（sector_code 为叶子节点 code）。"""
        return self._call("sector_constituents", sector_code=sector_code)

    def stock_sectors(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """单只股票所属指数/行业/概念。"""
        return self._call("stock_sectors", **self._stock_code_params(ts_code, code, symbol))

    def index_list_main(self):
        # type: () -> Dict[str, Any]
        """沪深主要指数列表。"""
        return self._call("index_list_main")

    def bj_list_stocks(self):
        # type: () -> Dict[str, Any]
        """京市股票列表。"""
        return self._call("bj_list_stocks")

    def bj_list_indices(self):
        # type: () -> Dict[str, Any]
        """京市指数列表。"""
        return self._call("bj_list_indices")

    def hk_list_stocks(self):
        # type: () -> Dict[str, Any]
        """港股列表。"""
        return self._call("hk_list_stocks")

    def kc_list_stocks(self):
        # type: () -> Dict[str, Any]
        """科创板股票列表。"""
        return self._call("kc_list_stocks")

    def fund_list_all(self):
        # type: () -> Dict[str, Any]
        """沪深基金列表。"""
        return self._call("fund_list_all")

    def fund_list_etf(self):
        # type: () -> Dict[str, Any]
        """ETF 基金列表。"""
        return self._call("fund_list_etf")

    # ========================================================================
    # 股池 (5)
    # ========================================================================

    def pool_limit_up(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """涨停股池（按日期 yyyy-MM-dd）。"""
        return self._call("pool_limit_up", trade_date=trade_date)

    def pool_limit_down(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """跌停股池（按日期）。"""
        return self._call("pool_limit_down", trade_date=trade_date)

    def pool_strong(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """强势股池（按日期）。"""
        return self._call("pool_strong", trade_date=trade_date)

    def pool_subnew(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """次新股池（按日期）。"""
        return self._call("pool_subnew", trade_date=trade_date)

    def pool_broken_board(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """炸板股池（按日期）。"""
        return self._call("pool_broken_board", trade_date=trade_date)

    # ========================================================================
    # 公司资料 (16)
    # ========================================================================

    def company_profile(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """公司简介。"""
        return self._call("company_profile", **self._stock_code_params(ts_code, code, symbol))

    def company_index_membership(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """所属指数。"""
        return self._call("company_index_membership", **self._stock_code_params(ts_code, code, symbol))

    def company_exec_history(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """历届高管。"""
        return self._call("company_exec_history", **self._stock_code_params(ts_code, code, symbol))

    def company_board_history(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """历届董事会。"""
        return self._call("company_board_history", **self._stock_code_params(ts_code, code, symbol))

    def company_supervisor_history(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """历届监事会。"""
        return self._call("company_supervisor_history", **self._stock_code_params(ts_code, code, symbol))

    def company_dividend(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """近年分红。"""
        return self._call("company_dividend", **self._stock_code_params(ts_code, code, symbol))

    def company_seo(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """近年增发。"""
        return self._call("company_seo", **self._stock_code_params(ts_code, code, symbol))

    def company_unlock(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """解禁限售。"""
        return self._call("company_unlock", **self._stock_code_params(ts_code, code, symbol))

    def company_quarter_profit(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """近一年季度利润。"""
        return self._call("company_quarter_profit", **self._stock_code_params(ts_code, code, symbol))

    def company_quarter_cashflow(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """近一年季度现金流。"""
        return self._call("company_quarter_cashflow", **self._stock_code_params(ts_code, code, symbol))

    def company_forecast(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """近年业绩预告。"""
        return self._call("company_forecast", **self._stock_code_params(ts_code, code, symbol))

    def company_finance_metrics(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """财务指标（近四季）。"""
        return self._call("company_finance_metrics", **self._stock_code_params(ts_code, code, symbol))

    def company_holders_top10(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """十大股东。"""
        return self._call("company_holders_top10", **self._stock_code_params(ts_code, code, symbol))

    def company_float_holders_top10(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """十大流通股东。"""
        return self._call("company_float_holders_top10", **self._stock_code_params(ts_code, code, symbol))

    def company_holder_trend(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """股东户数变化。"""
        return self._call("company_holder_trend", **self._stock_code_params(ts_code, code, symbol))

    def company_fund_holdings(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """基金持股。"""
        return self._call("company_fund_holdings", **self._stock_code_params(ts_code, code, symbol))

    # ========================================================================
    # 实时与逐笔 (6)
    # ========================================================================

    def stock_realtime(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """实时行情（网络源，6 位代码）。"""
        return self._call("stock_realtime", **self._stock_code_params(ts_code, code, symbol))

    def stock_ticks_today(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """当日逐笔成交。"""
        return self._call("stock_ticks_today", **self._stock_code_params(ts_code, code, symbol))

    def stock_realtime_multi(self, stock_codes):
        # type: (str) -> Dict[str, Any]
        """多股实时行情（英文逗号分隔，至多 20 只）。"""
        return self._call("stock_realtime_multi", stock_codes=stock_codes)

    def quote_realtime_broker(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """实时行情（专业行情源，6 位代码）。"""
        return self._call("quote_realtime_broker", **self._stock_code_params(ts_code, code, symbol))

    def quote_five_broker(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """买卖五档（专业行情源）。"""
        return self._call("quote_five_broker", **self._stock_code_params(ts_code, code, symbol))

    def capital_flow_history(self, ts_code=None, code=None, symbol=None, st=None, et=None, lt=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[str], Optional[int]) -> Dict[str, Any]
        """资金流向历史（可选 st、et、lt）。"""
        params = self._stock_code_params(ts_code, code, symbol)
        if st:
            params["st"] = st
        if et:
            params["et"] = et
        if lt:
            params["lt"] = lt
        return self._call("capital_flow_history", **params)

    # ========================================================================
    # K 线 / 分时 (5)
    # ========================================================================

    def quote_bars_latest(self, full_code, interval="d", cq="n", lt=5):
        # type: (str, str, str, int) -> Dict[str, Any]
        """最新 K 线/分时（lt 最多 5）。"""
        return self._call("quote_bars_latest", full_code=full_code, interval=interval, cq=cq, lt=lt)

    def quote_bars_history(self, full_code, interval="d", cq="n", st=None, et=None, lt=None):
        # type: (str, str, str, Optional[str], Optional[str], Optional[int]) -> Dict[str, Any]
        """历史 K 线/分时（可选 st、et、lt）。"""
        params = {"full_code": full_code, "interval": interval, "cq": cq}
        if st:
            params["st"] = st
        if et:
            params["et"] = et
        if lt:
            params["lt"] = lt
        return self._call("quote_bars_history", **params)

    def quote_stop_prices(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """历史涨跌停价（可选 st、et）。"""
        params = {"full_code": full_code}
        if st:
            params["st"] = st
        if et:
            params["et"] = et
        return self._call("quote_stop_prices", **params)

    def quote_market_indicators(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """行情指标（量比、短周期涨幅等，可选 st、et）。"""
        params = {"full_code": full_code}
        if st:
            params["st"] = st
        if et:
            params["et"] = et
        return self._call("quote_market_indicators", **params)

    def stock_instrument(self, full_code):
        # type: (str) -> Dict[str, Any]
        """股票基础信息（涨跌停价、股本等）。"""
        return self._call("stock_instrument", full_code=full_code)

    # ========================================================================
    # 财务报表 (8)
    # ========================================================================

    def _fin_call(self, api, full_code, st=None, et=None):
        # type: (str, str, Optional[str], Optional[str]) -> Dict[str, Any]
        params = {"full_code": full_code}
        if st:
            params["st"] = st
        if et:
            params["et"] = et
        return self._call(api, **params)

    def fin_balance_sheet(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """资产负债表。"""
        return self._fin_call("fin_balance_sheet", full_code, st, et)

    def fin_income_statement(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """利润表。"""
        return self._fin_call("fin_income_statement", full_code, st, et)

    def fin_cashflow_statement(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """现金流量表。"""
        return self._fin_call("fin_cashflow_statement", full_code, st, et)

    def fin_per_share_index(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """财务主要指标。"""
        return self._fin_call("fin_per_share_index", full_code, st, et)

    def fin_capital_structure(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """公司股本表。"""
        return self._fin_call("fin_capital_structure", full_code, st, et)

    def fin_top10_holders(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """公司十大股东（财报口径）。"""
        return self._fin_call("fin_top10_holders", full_code, st, et)

    def fin_top10_float_holders(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """公司十大流通股东（财报口径）。"""
        return self._fin_call("fin_top10_float_holders", full_code, st, et)

    def fin_holder_counts(self, full_code, st=None, et=None):
        # type: (str, Optional[str], Optional[str]) -> Dict[str, Any]
        """公司股东数。"""
        return self._fin_call("fin_holder_counts", full_code, st, et)

    # ========================================================================
    # 技术指标 (5)
    # ========================================================================

    def _tech_call(self, api, full_code, interval="d", cq="n"):
        # type: (str, str, str, str) -> Dict[str, Any]
        return self._call(api, full_code=full_code, interval=interval, cq=cq)

    def tech_macd(self, full_code, interval="d", cq="n"):
        # type: (str, str, str) -> Dict[str, Any]
        """MACD 技术指标。"""
        return self._tech_call("tech_macd", full_code, interval, cq)

    def tech_ma(self, full_code, interval="d", cq="n"):
        # type: (str, str, str) -> Dict[str, Any]
        """均线 MA。"""
        return self._tech_call("tech_ma", full_code, interval, cq)

    def tech_boll(self, full_code, interval="d", cq="n"):
        # type: (str, str, str) -> Dict[str, Any]
        """BOLL 技术指标。"""
        return self._tech_call("tech_boll", full_code, interval, cq)

    def tech_kdj(self, full_code, interval="d", cq="n"):
        # type: (str, str, str) -> Dict[str, Any]
        """KDJ 技术指标。"""
        return self._tech_call("tech_kdj", full_code, interval, cq)

    # === 兼容旧版简易均线 ===
    def stock_ma(self, ts_code=None, code=None, symbol=None, period="5m"):
        # type: (Optional[str], Optional[str], Optional[str], str) -> Dict[str, Any]
        """均线（兼容旧版 path，period 如 5m、dn）。"""
        params = self._stock_code_params(ts_code, code, symbol)
        params["period"] = period
        return self._call("stock_ma", **params)

    # ========================================================================
    # 指数 (8)
    # ========================================================================

    def index_realtime_broker(self, index_code):
        # type: (str) -> Dict[str, Any]
        """指数实时行情（index_code 如 000001.SH）。"""
        return self._call("index_realtime_broker", index_code=index_code)

    def index_bars_latest(self, index_full, interval="d", lt=5):
        # type: (str, str, int) -> Dict[str, Any]
        """指数最新 K 线（lt 最多 5）。"""
        return self._call("index_bars_latest", index_full=index_full, interval=interval, lt=lt)

    def index_bars_history(self, index_full, interval="d", st=None, et=None):
        # type: (str, str, Optional[str], Optional[str]) -> Dict[str, Any]
        """指数历史 K 线（可选 st、et）。"""
        params = {"index_full": index_full, "interval": interval}
        if st:
            params["st"] = st
        if et:
            params["et"] = et
        return self._call("index_bars_history", **params)

    def _index_tech_call(self, api, index_code, interval="d"):
        # type: (str, str, str) -> Dict[str, Any]
        return self._call(api, index_code=index_code, interval=interval)

    def index_tech_macd(self, index_code, interval="d"):
        # type: (str, str) -> Dict[str, Any]
        """指数 MACD。"""
        return self._index_tech_call("index_tech_macd", index_code, interval)

    def index_tech_ma(self, index_code, interval="d"):
        # type: (str, str) -> Dict[str, Any]
        """指数 MA。"""
        return self._index_tech_call("index_tech_ma", index_code, interval)

    def index_tech_boll(self, index_code, interval="d"):
        # type: (str, str) -> Dict[str, Any]
        """指数 BOLL。"""
        return self._index_tech_call("index_tech_boll", index_code, interval)

    def index_tech_kdj(self, index_code, interval="d"):
        # type: (str, str) -> Dict[str, Any]
        """指数 KDJ。"""
        return self._index_tech_call("index_tech_kdj", index_code, interval)

    # ========================================================================
    # 京市/港股/科创板/基金 实时 (7)
    # ========================================================================

    def bj_quote_realtime(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """京市股票实时行情。"""
        return self._call("bj_quote_realtime", **self._stock_code_params(ts_code, code, symbol))

    def bj_quote_five(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """京市五档行情。"""
        return self._call("bj_quote_five", **self._stock_code_params(ts_code, code, symbol))

    def hk_quote_realtime(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """港股实时行情。"""
        return self._call("hk_quote_realtime", **self._stock_code_params(ts_code, code, symbol))

    def hk_quote_five(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """港股五档行情。"""
        return self._call("hk_quote_five", **self._stock_code_params(ts_code, code, symbol))

    def kc_quote_realtime(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """科创板实时行情。"""
        return self._call("kc_quote_realtime", **self._stock_code_params(ts_code, code, symbol))

    def kc_quote_five(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """科创板五档行情。"""
        return self._call("kc_quote_five", **self._stock_code_params(ts_code, code, symbol))

    def fund_quote_realtime(self, ts_code=None, code=None, symbol=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> Dict[str, Any]
        """基金实时行情。"""
        return self._call("fund_quote_realtime", **self._stock_code_params(ts_code, code, symbol))

    # ========================================================================
    # 全市场实时 (1)
    # ========================================================================

    def market_realtime_all_network(self):
        # type: () -> Dict[str, Any]
        """全市场实时（网络源，高阶套餐，限频）。"""
        return self._call("market_realtime_all_network")

    # ========================================================================
    # 龙虎榜 / 游资 (5)
    # ========================================================================

    def dragon_tiger(self, date):
        # type: (str) -> Dict[str, Any]
        """龙虎榜查询（date: YYYY-MM-DD）。"""
        return self._call("dragonTiger", date=date)

    def youzi_all(self, date):
        # type: (str) -> Dict[str, Any]
        """全量游资上榜交割单历史（date: YYYY-MM-DD）。"""
        return self._call("youzi_all", date=date)

    def youzi_by_name(self, yzmc, date):
        # type: (str, str) -> Dict[str, Any]
        """按游资名称查询上榜交割单。"""
        return self._call("youzi_jgdhis", yzmc=yzmc, date=date)

    def youzi_gegu(self, code, start_date, end_date):
        # type: (str, str, str) -> Dict[str, Any]
        """个股游资上榜交割单。"""
        return self._call("youzi_gegu", code=code, startDate=start_date, endDate=end_date)

    def youzi_name(self):
        # type: () -> Dict[str, Any]
        """获取全部游资名称列表。"""
        return self._call("youzi_name")

    # ========================================================================
    # 早盘竞价 (13)
    # ========================================================================

    def base_bkjj(self, start_date, end_date, type_):
        # type: (str, str, str) -> Dict[str, Any]
        """早盘热点板块竞价。"""
        return self._call("base_bkjj", startDate=start_date, endDate=end_date, type=type_)

    def base_bkjjzq(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """增强版热点板块竞价。"""
        return self._call("base_bkjjzq", tradeDate=trade_date)

    def base_zqbk_code_list(self, trade_date, bk_code):
        # type: (str, str) -> Dict[str, Any]
        """增强版热点板块竞价所属个股。"""
        return self._call("base_zqbk_code_list", tradeDate=trade_date, bkCode=bk_code)

    def base_bk_code_list(self, start_date, end_date, bk_code):
        # type: (str, str, str) -> Dict[str, Any]
        """早盘热点板块竞价所属个股。"""
        return self._call("base_bk_code_list", startDate=start_date, endDate=end_date, bkCode=bk_code)

    # === 早盘抢筹 ===
    def base_jjqc(self, trade_date, period, type_):
        # type: (str, str, str) -> Dict[str, Any]
        """早盘抢筹委托金额排序。"""
        return self._call("base_jjqc", tradeDate=trade_date, period=period, type=type_)

    def base_jjqc_cje(self, trade_date, period):
        # type: (str, str) -> Dict[str, Any]
        """早盘抢筹成交金额排序。"""
        return self._call("base_jjqc_cje", tradeDate=trade_date, period=period)

    def base_jjqc_open(self, trade_date, period):
        # type: (str, str) -> Dict[str, Any]
        """早盘抢筹开盘金额排序。"""
        return self._call("base_jjqc_open", tradeDate=trade_date, period=period)

    def base_jjqc_zf(self, trade_date, period):
        # type: (str, str) -> Dict[str, Any]
        """早盘抢筹涨幅排序。"""
        return self._call("base_jjqc_zf", tradeDate=trade_date, period=period)

    # === 尾盘抢筹 ===
    def base_jjqc_tail_wt(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """尾盘抢筹委托金额排序。"""
        return self._call("base_jjqc_tail_wt", tradeDate=trade_date)

    def base_jjqc_tail_cje(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """尾盘抢筹成交金额排序。"""
        return self._call("base_jjqc_tail_cje", tradeDate=trade_date)

    def base_jjqc_tail_close(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """尾盘抢筹收盘金额排序。"""
        return self._call("base_jjqc_tail_close", tradeDate=trade_date)

    def base_jjqc_tail_zf(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """尾盘抢筹涨幅排序。"""
        return self._call("base_jjqc_tail_zf", tradeDate=trade_date)

    # === 竞价一字板 ===
    def jjyizi_list(self, trade_date):
        # type: (str) -> Dict[str, Any]
        """竞价一字板。"""
        return self._call("jjyizi_list", tradeDate=trade_date)

    # ========================================================================
    # 基础数据 (4)
    # ========================================================================

    def base_st(self):
        # type: () -> Dict[str, Any]
        """ST 股票列表。"""
        return self._call("base_st")

    def base_gn(self):
        # type: () -> Dict[str, Any]
        """概念代码列表。"""
        return self._call("base_gn")

    def base_bk(self):
        # type: () -> Dict[str, Any]
        """板块代码列表。"""
        return self._call("base_bk")

    def base_emotional_cycle(self):
        # type: () -> Dict[str, Any]
        """情绪周期数据。"""
        return self._call("base_emotional_cycle")

    # ========================================================================
    # 板块资金流与成分 (3)
    # ========================================================================

    def base_bk_flow_history(self, bk_code):
        # type: (str) -> Dict[str, Any]
        """板块/概念历史资金流。"""
        return self._call("base_bk_flow_history", bkCode=bk_code)

    def base_bk_list(self, bk_code, page_no, page_size):
        # type: (str, int, int) -> Dict[str, Any]
        """板块/概念成分股列表。"""
        return self._call("base_bk_list", bkCode=bk_code, pageNo=str(page_no), pageSize=str(page_size))

    def base_code_flow(self, code, start_date, end_date, page_no, page_size):
        # type: (str, str, str, int, int) -> Dict[str, Any]
        """个股资金流向。"""
        return self._call(
            "base_code_flow",
            code=code,
            startDate=start_date,
            endDate=end_date,
            pageNo=str(page_no),
            pageSize=str(page_size),
        )

    # ========================================================================
    # 异动数据 (3)
    # ========================================================================

    def change_all_history(self, start_date, end_date, type_):
        # type: (str, str, str) -> Dict[str, Any]
        """全量异动数据历史。"""
        return self._call("change_all_history", startDate=start_date, endDate=end_date, type=type_)

    def change_code_history(self, code, start_date, end_date):
        # type: (str, str, str) -> Dict[str, Any]
        """股票异动数据历史。"""
        return self._call("change_code_history", code=code, startDate=start_date, endDate=end_date)

    def change_ren_qi(self):
        # type: () -> Dict[str, Any]
        """股票人气排行榜。"""
        return self._call("change_ren_qi")

    # ========================================================================
    # 风险监控 (4)
    # ========================================================================

    def alarm_data(self, trade_date, type_, code=None):
        # type: (str, str, Optional[str]) -> Dict[str, Any]
        """大股东减持。"""
        params = {"tradeDate": trade_date, "type": type_}
        if code:
            params["code"] = code
        return self._call("alarm_data", **params)

    def alarm_data_unlock(self, trade_date, type_, code=None):
        # type: (str, str, Optional[str]) -> Dict[str, Any]
        """大比例解禁。"""
        params = {"tradeDate": trade_date, "type": type_}
        if code:
            params["code"] = code
        return self._call("alarm_data_unlock", **params)

    def alarm_data_risk(self, trade_date, type_, code=None):
        # type: (str, str, Optional[str]) -> Dict[str, Any]
        """风险监控。"""
        params = {"tradeDate": trade_date, "type": type_}
        if code:
            params["code"] = code
        return self._call("alarm_data_risk", **params)

    def alarm_data_serious(self, trade_date, type_, code=None):
        # type: (str, str, Optional[str]) -> Dict[str, Any]
        """严重异动提醒。"""
        params = {"tradeDate": trade_date, "type": type_}
        if code:
            params["code"] = code
        return self._call("alarm_data_serious", **params)


# 便捷函数
def call(api, token=None, base_url=None, **params):
    # type: (str, Optional[str], Optional[str], **Any) -> Dict[str, Any]
    """快捷调用网关（无需创建 Client 实例）。

    参数
    ----
    api : str
        接口别名。
    token : str, optional
        Token；未传时从环境变量读取。
    base_url : str, optional
        网关地址；未传时从环境变量读取。
    **params
        业务参数。

    返回
    ----
    dict
        平台 JSON 响应。
    """
    return call_gateway(api=api, token=token, base_url=base_url, **params)