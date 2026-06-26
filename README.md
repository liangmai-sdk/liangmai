# 量脉 (Liangmai) Python SDK — 金融数据平台

<p align="center">
  <b>封装量脉金融数据平台全部 105 个接口</b><br>
  沪深 A 股 · 指数 · 基金 · 港股 · 科创板 · 京市 · 龙虎榜 · 游资 · 早盘竞价 · 板块资金流 · 异动监控
</p>

<p align="center">
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/v/liangmai?label=PyPI&color=blue" alt="PyPI"></a>
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/pyversions/liangmai" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/dm/liangmai" alt="Downloads"></a>
</p>

---

## 平台简介

**量脉**（liangmai.pro）是一个专业的金融数据平台，提供沪深京 A 股、指数、基金、港股、科创板、京市、龙虎榜、游资上榜、早盘竞价、板块资金流、异动监控等全线金融数据接口。

本 SDK 是量脉平台的官方 Python 客户端，封装了平台**全部 105 个 API 接口**，支持 Python 3.8 及以上版本。

```python
>>> from liangmai import API_COUNT
>>> print(f"量脉平台接口总数: {API_COUNT}")
量脉平台接口总数: 105
```

## 安装

```bash
pip install liangmai
```

要求 Python >= 3.8

## 快速开始

```python
from liangmai import Client

# 创建客户端
client = Client(token="your_platform_token")
# 也可通过环境变量 LIANGMAI_TOKEN 自动读取

# 获取沪深京股票列表
stocks = client.stock_list()

# 查询实时行情
realtime = client.stock_realtime(ts_code="601012")

# 查询涨停股池
limit_up = client.pool_limit_up(trade_date="2025-06-26")

# 查询历史 K 线（日线，前复权，100 条）
bars = client.quote_bars_history(
    full_code="000001.SZ",
    interval="d",
    cq="n",
    lt=100,
)

# 查询龙虎榜
dragon = client.dragon_tiger(date="2025-06-26")

# 查询早盘热点板块竞价
bkjj = client.base_bkjj(
    start_date="2025-06-26",
    end_date="2025-06-26",
    type_="1",
)

# 查询游资全部上榜记录
youzi = client.youzi_all(date="2025-06-26")

# 查询指数实时行情
index = client.index_realtime_broker(index_code="000001.SH")

# 全市场实时快照（高阶套餐）
market = client.market_realtime_all_network()
```

## 接口全览（105 个）

### 列表与日历（13 个）
`stock_list` · `hs_list_main` · `ipo_calendar` · `sector_tree` · `sector_constituents` · `stock_sectors` · `index_list_main` · `bj_list_stocks` · `bj_list_indices` · `hk_list_stocks` · `kc_list_stocks` · `fund_list_all` · `fund_list_etf`

### 股池（5 个）
`pool_limit_up` · `pool_limit_down` · `pool_strong` · `pool_subnew` · `pool_broken_board`

### 公司资料（16 个）
`company_profile` · `company_index_membership` · `company_exec_history` · `company_board_history` · `company_supervisor_history` · `company_dividend` · `company_seo` · `company_unlock` · `company_quarter_profit` · `company_quarter_cashflow` · `company_forecast` · `company_finance_metrics` · `company_holders_top10` · `company_float_holders_top10` · `company_holder_trend` · `company_fund_holdings`

### 实时行情与逐笔（6 个）
`stock_realtime` · `stock_ticks_today` · `stock_realtime_multi` · `quote_realtime_broker` · `quote_five_broker` · `capital_flow_history`

### K 线/分时（5 个）
`quote_bars_latest` · `quote_bars_history` · `quote_stop_prices` · `quote_market_indicators` · `stock_instrument`

### 财务报表（8 个）
`fin_balance_sheet` · `fin_income_statement` · `fin_cashflow_statement` · `fin_per_share_index` · `fin_capital_structure` · `fin_top10_holders` · `fin_top10_float_holders` · `fin_holder_counts`

### 技术指标（5 个）
`tech_macd` · `tech_ma` · `tech_boll` · `tech_kdj` · `stock_ma`

### 指数（8 个）
`index_realtime_broker` · `index_bars_latest` · `index_bars_history` · `index_tech_macd` · `index_tech_ma` · `index_tech_boll` · `index_tech_kdj`

### 京市/港股/科创板/基金实时（7 个）
`bj_quote_realtime` · `bj_quote_five` · `hk_quote_realtime` · `hk_quote_five` · `kc_quote_realtime` · `kc_quote_five` · `fund_quote_realtime`

### 全市场实时（1 个）
`market_realtime_all_network`

### 龙虎榜与游资（5 个）
`dragon_tiger` · `youzi_all` · `youzi_by_name` · `youzi_gegu` · `youzi_name`

### 早盘竞价（13 个）
`base_bkjj` · `base_bkjjzq` · `base_zqbk_code_list` · `base_bk_code_list` · `base_jjqc` · `base_jjqc_cje` · `base_jjqc_open` · `base_jjqc_zf` · `base_jjqc_tail_wt` · `base_jjqc_tail_cje` · `base_jjqc_tail_close` · `base_jjqc_tail_zf` · `jjyizi_list`

### 基础数据（4 个）
`base_st` · `base_gn` · `base_bk` · `base_emotional_cycle`

### 板块资金流与成分（3 个）
`base_bk_flow_history` · `base_bk_list` · `base_code_flow`

### 异动数据（3 个）
`change_all_history` · `change_code_history` · `change_ren_qi`

### 风险监控（4 个）
`alarm_data` · `alarm_data_unlock` · `alarm_data_risk` · `alarm_data_serious`

---

## 环境变量配置

```bash
# Linux / Mac
export LIANGMAI_TOKEN=your_platform_token
export LIANGMAI_BASE_URL=https://liangmai.pro/api/gateway  # 可选

# Windows PowerShell
$env:LIANGMAI_TOKEN="your_platform_token"
```

```python
import os
os.environ["LIANGMAI_TOKEN"] = "your_token"

from liangmai import Client
client = Client()  # 自动从环境变量读取
```

## 快捷调用

无需创建 Client 实例，直接调用网关：

```python
from liangmai import call

data = call("stock_realtime", ts_code="601012", token="your_token")
```

## 错误处理

```python
try:
    client = Client(token="your_token")
    data = client.stock_realtime(ts_code="000001")
except RuntimeError as e:
    print(f"请求失败: {e}")
```

## 常见问题

**Q: 股票代码格式？**  
A: 支持 6 位代码（如 `"000001"`）和带市场后缀（如 `"000001.SZ"`），网关会自动处理。K 线接口的 `full_code` 需带市场后缀。

**Q: 日期格式？**  
A: 股池类接口用 `yyyy-MM-dd`（如 `"2025-06-26"`），K 线类 `st`/`et` 用 `YYYYMMDD` 或 `YYYYMMDDhhmmss`。

**Q: 最新 K 线条数限制？**  
A: `_latest` 后缀的接口 `lt` 最多 5 条，要更多条请使用 `_history` 后缀的接口。

**Q: Token 从哪里获取？**  
A: 登录量脉平台 [liangmai.pro](https://liangmai.pro) 获取。

## 相关链接

- **量脉平台**: [https://liangmai.pro](https://liangmai.pro)
- **PyPI 包**: [https://pypi.org/project/liangmai/](https://pypi.org/project/liangmai/)
- **GitHub 仓库**: [https://github.com/liangmai-sdk/liangmai](https://github.com/liangmai-sdk/liangmai)
- **问题反馈**: [https://github.com/liangmai-sdk/liangmai/issues](https://github.com/liangmai-sdk/liangmai/issues)

## 许可证

MIT License