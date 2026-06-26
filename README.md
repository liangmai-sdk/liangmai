# 量脉 (Liangmai) Python SDK — 金融数据平台

封装量脉金融数据平台 **全部 105 个接口**，覆盖沪深京 A 股、指数、基金、可转债、期货、龙虎榜、早盘竞价、游资、板块资金流、异动监控等全线数据。

```python
>>> from liangmai import API_COUNT
>>> print(API_COUNT)
105
```

## 安装

```bash
pip install liangmai
```

需要 Python >= 3.8

## 快速开始

```python
from liangmai import Client

client = Client(token="your_platform_token")

# 股票列表
data = client.stock_list()

# 实时行情
data = client.stock_realtime(ts_code="601012")

# 涨停股池
data = client.pool_limit_up(trade_date="2025-04-01")

# 历史 K 线
data = client.quote_bars_history(full_code="000001.SZ", interval="d", lt=100)

# 龙虎榜
data = client.dragon_tiger(date="2025-04-01")

# 早盘竞价
data = client.base_bkjj(start_date="2025-04-01", end_date="2025-04-01", type_="1")

# 游资上榜
data = client.youzi_all(date="2025-04-01")
```

## 105 个接口全览

### 列表与日历 (13)
`stock_list` · `hs_list_main` · `ipo_calendar` · `sector_tree` · `sector_constituents` · `stock_sectors` · `index_list_main` · `bj_list_stocks` · `bj_list_indices` · `hk_list_stocks` · `kc_list_stocks` · `fund_list_all` · `fund_list_etf`

### 股池 (5)
`pool_limit_up` · `pool_limit_down` · `pool_strong` · `pool_subnew` · `pool_broken_board`

### 公司资料 (16)
`company_profile` · `company_index_membership` · `company_exec_history` · `company_board_history` · `company_supervisor_history` · `company_dividend` · `company_seo` · `company_unlock` · `company_quarter_profit` · `company_quarter_cashflow` · `company_forecast` · `company_finance_metrics` · `company_holders_top10` · `company_float_holders_top10` · `company_holder_trend` · `company_fund_holdings`

### 实时行情与逐笔 (6)
`stock_realtime` · `stock_ticks_today` · `stock_realtime_multi` · `quote_realtime_broker` · `quote_five_broker` · `capital_flow_history`

### K 线/分时 (5)
`quote_bars_latest` · `quote_bars_history` · `quote_stop_prices` · `quote_market_indicators` · `stock_instrument`

### 财务报表 (8)
`fin_balance_sheet` · `fin_income_statement` · `fin_cashflow_statement` · `fin_per_share_index` · `fin_capital_structure` · `fin_top10_holders` · `fin_top10_float_holders` · `fin_holder_counts`

### 技术指标 (5)
`tech_macd` · `tech_ma` · `tech_boll` · `tech_kdj` · `stock_ma`

### 指数 (8)
`index_realtime_broker` · `index_bars_latest` · `index_bars_history` · `index_tech_macd` · `index_tech_ma` · `index_tech_boll` · `index_tech_kdj`

### 京市/港股/科创/基金 实时 (7)
`bj_quote_realtime` · `bj_quote_five` · `hk_quote_realtime` · `hk_quote_five` · `kc_quote_realtime` · `kc_quote_five` · `fund_quote_realtime`

### 全市场实时 (1)
`market_realtime_all_network`

### 龙虎榜与游资 (5)
`dragon_tiger` · `youzi_all` · `youzi_by_name` · `youzi_gegu` · `youzi_name`

### 早盘竞价 (13)
`base_bkjj` · `base_bkjjzq` · `base_zqbk_code_list` · `base_bk_code_list` · `base_jjqc` · `base_jjqc_cje` · `base_jjqc_open` · `base_jjqc_zf` · `base_jjqc_tail_wt` · `base_jjqc_tail_cje` · `base_jjqc_tail_close` · `base_jjqc_tail_zf` · `jjyizi_list`

### 基础数据 (4)
`base_st` · `base_gn` · `base_bk` · `base_emotional_cycle`

### 板块资金流与成分 (3)
`base_bk_flow_history` · `base_bk_list` · `base_code_flow`

### 异动数据 (3)
`change_all_history` · `change_code_history` · `change_ren_qi`

### 风险监控 (4)
`alarm_data` · `alarm_data_unlock` · `alarm_data_risk` · `alarm_data_serious`

> 以上 105 个接口均来自平台 `mairui_alias` + `stockapi_alias` 配置文件，与网关 `/api/gateway` 完全对齐。

## 环境变量

```bash
export LIANGMAI_TOKEN=your_platform_token
export LIANGMAI_BASE_URL=https://liangmai.pro/api/gateway  # 可选，默认值
```

## 许可证

MIT License