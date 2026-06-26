<p align="center">
  <h1 align="center">量脉 · 金融数据平台</h1>
  <h3 align="center">官方 Python SDK</h3>
</p>

<p align="center">
  <b>105 个金融数据 API · 毫秒级响应 · 多市场全覆盖 · 量化交易就绪</b>
</p>

<p align="center">
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/v/liangmai?label=PyPI&color=blue" alt="PyPI"></a>
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/pyversions/liangmai" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/dm/liangmai" alt="Downloads"></a>
</p>

---

## 为什么选择量脉

量脉是一个**企业级金融数据平台**，为量化交易、金融分析、AI 投资决策提供底层数据支撑。我们不只是"数据接口"——我们提供的是**经过清洗、标准化、多源校验的生产级金融数据服务**。

| 能力 | 详情 |
|------|------|
| 📊 **数据广度** | 沪深京 A 股 5000+ 标的、2000+ 指数、300+ ETF、全部板块与概念 |
| 🚀 **响应速度** | 毫秒级实时行情推送，历史数据秒级返回 |
| 🔄 **数据一致性** | 多源数据融合+自动校验，杜绝脏数据 |
| 🛡️ **高可用** | 多节点部署，99.9% 可用性 SLA |
| 🤖 **AI 就绪** | 标准 RESTful API，Token 鉴权，限流防滥用，为 AI Agent 调用而生 |
| 📦 **开箱即用** | 官方 Python SDK 封装全部接口，`pip install` 一行即可 |

## 平台数据覆盖

```
📈 沪深 A 股        5000+ 标的    实时行情 · K线 · 逐笔 · 资金流 · 财务
📊 指数              2000+ 标的    实时 · K线 · 技术指标 MACD/MA/BOLL/KDJ
🏦 科创板 / 京市     全量覆盖      实时行情 · 五档买卖
🇭🇰 港股              全量覆盖      实时行情 · 五档买卖
💰 基金 / ETF         300+ 标的    实时行情
🐉 龙虎榜             全量历史      上榜明细 · 游资追踪
🧨 早盘竞价           实时推送      热点板块 · 抢筹排序 · 一字板
⚡ 异动监控           实时推送      全量异动 · 个股异动 · 人气排行
🛡️ 风险预警           实时推送      减持 · 解禁 · 严重异动
```

## 快速安装

```bash
pip install liangmai
```

> 最低 Python 版本要求：3.8  
> 零额外依赖：仅需 `requests`

## 代码示例

```python
from liangmai import Client, API_COUNT

print(f"量脉平台接口总数: {API_COUNT}")  # 105

# 创建客户端（支持环境变量自动读取 Token）
client = Client(token="your_platform_token")

# ---- 股票列表 ----
stocks = client.stock_list()

# ---- 实时行情 ----
realtime = client.stock_realtime(ts_code="601012")
multi = client.stock_realtime_multi("000001,600519,300750")

# ---- 涨停/跌停/强势/次新/炸板 股池 ----
limit_up = client.pool_limit_up(trade_date="2025-06-26")
limit_down = client.pool_limit_down(trade_date="2025-06-26")
strong = client.pool_strong(trade_date="2025-06-26")

# ---- K线（最新 + 历史）----
bars_latest = client.quote_bars_latest(full_code="000001.SZ", interval="d", cq="n", lt=5)
bars_history = client.quote_bars_history(full_code="000001.SZ", interval="d", cq="n", lt=100)

# ---- 财务数据 ----
balance = client.fin_balance_sheet(full_code="000001.SZ")
income = client.fin_income_statement(full_code="000001.SZ")
cashflow = client.fin_cashflow_statement(full_code="000001.SZ")

# ---- 龙虎榜 & 游资 ----
dragon = client.dragon_tiger(date="2025-06-26")
youzi = client.youzi_all(date="2025-06-26")
youzi_names = client.youzi_name()

# ---- 早盘竞价 ----
bkjj = client.base_bkjj(start_date="2025-06-26", end_date="2025-06-26", type_="1")
jjqc = client.base_jjqc(trade_date="2025-06-26", period="1", type_="1")

# ---- 异动监控 & 风险预警 ----
changes = client.change_all_history(start_date="2025-06-01", end_date="2025-06-26", type_="1")
alarms = client.alarm_data(trade_date="2025-06-26", type_="1")

# ---- 情绪周期 ----
emotion = client.base_emotional_cycle()
```

## 105 个接口全览

### 📋 列表与日历（13）
`stock_list` `hs_list_main` `ipo_calendar` `sector_tree` `sector_constituents` `stock_sectors` `index_list_main` `bj_list_stocks` `bj_list_indices` `hk_list_stocks` `kc_list_stocks` `fund_list_all` `fund_list_etf`

### 📊 股池（5）
`pool_limit_up` `pool_limit_down` `pool_strong` `pool_subnew` `pool_broken_board`

### 🏢 公司资料（16）
`company_profile` `company_index_membership` `company_exec_history` `company_board_history` `company_supervisor_history` `company_dividend` `company_seo` `company_unlock` `company_quarter_profit` `company_quarter_cashflow` `company_forecast` `company_finance_metrics` `company_holders_top10` `company_float_holders_top10` `company_holder_trend` `company_fund_holdings`

### 📈 实时行情与逐笔（6）
`stock_realtime` `stock_ticks_today` `stock_realtime_multi` `quote_realtime_broker` `quote_five_broker` `capital_flow_history`

### 🕯️ K线/分时（5）
`quote_bars_latest` `quote_bars_history` `quote_stop_prices` `quote_market_indicators` `stock_instrument`

### 📑 财务报表（8）
`fin_balance_sheet` `fin_income_statement` `fin_cashflow_statement` `fin_per_share_index` `fin_capital_structure` `fin_top10_holders` `fin_top10_float_holders` `fin_holder_counts`

### 🔬 技术指标（5）
`tech_macd` `tech_ma` `tech_boll` `tech_kdj` `stock_ma`

### 📉 指数（8）
`index_realtime_broker` `index_bars_latest` `index_bars_history` `index_tech_macd` `index_tech_ma` `index_tech_boll` `index_tech_kdj`

### 🌏 京市/港股/科创/基金实时（7）
`bj_quote_realtime` `bj_quote_five` `hk_quote_realtime` `hk_quote_five` `kc_quote_realtime` `kc_quote_five` `fund_quote_realtime`

### 🌐 全市场实时（1）
`market_realtime_all_network`

### 🐉 龙虎榜与游资（5）
`dragon_tiger` `youzi_all` `youzi_by_name` `youzi_gegu` `youzi_name`

### 🧨 早盘竞价（13）
`base_bkjj` `base_bkjjzq` `base_zqbk_code_list` `base_bk_code_list` `base_jjqc` `base_jjqc_cje` `base_jjqc_open` `base_jjqc_zf` `base_jjqc_tail_wt` `base_jjqc_tail_cje` `base_jjqc_tail_close` `base_jjqc_tail_zf` `jjyizi_list`

### 🔧 基础数据（4）
`base_st` `base_gn` `base_bk` `base_emotional_cycle`

### 💸 板块资金流与成分（3）
`base_bk_flow_history` `base_bk_list` `base_code_flow`

### ⚡ 异动数据（3）
`change_all_history` `change_code_history` `change_ren_qi`

### 🛡️ 风险监控（4）
`alarm_data` `alarm_data_unlock` `alarm_data_risk` `alarm_data_serious`

---

## SDK 工程设计

```python
from liangmai import Client, API_COUNT, call
# API_COUNT = 105  ← 导入即知接口总数，IDE 自动补全

client = Client(
    token="your_token",           # 平台 Token
    base_url="https://liangmai.pro/api/gateway",  # 可选，默认即此
    timeout=30,                    # 请求超时（秒）
)

# 智能重试：5xx 错误自动重试一次（与平台文档页行为一致）
# 参数别名：ts_code / code / symbol 均可
# 市场后缀自动补全：600000 → 600000.SH，300750 → 300750.SZ
```

### 架构特性

| 特性 | 说明 |
|------|------|
| 🔄 **自动重试** | 5xx / code=500 时自动重试，与平台文档页 `fetchGatewayWithRetry` 对齐 |
| 🏷️ **参数别名** | `ts_code` / `code` / `symbol` 三选一，`trade_date` / `date` 混用 |
| 📝 **市场后缀补全** | 传 6 位代码自动推断 `.SZ` / `.SH` / `.BJ` |
| 🔧 **环境变量** | `LIANGMAI_TOKEN` + `LIANGMAI_BASE_URL`，12-Factor App 友好 |
| 📦 **零臃肿** | 只依赖 `requests`，不引入 pandas/numpy 等重型库 |
| 🐍 **全版本** | Python 3.8 ~ 3.14 全面支持 |
| 🤖 **AI 友好** | 标准类型注解 + 完整 docstring，AI Agent 可直接理解调用 |

## 环境变量

```bash
# Linux / macOS
export LIANGMAI_TOKEN=your_platform_token
export LIANGMAI_BASE_URL=https://liangmai.pro/api/gateway

# Windows PowerShell
$env:LIANGMAI_TOKEN="your_platform_token"
```

## 快捷调用

```python
from liangmai import call

data = call("stock_realtime", ts_code="601012", token="your_token")
```

## AI Agent 调用示例

```python
import os
from liangmai import Client, API_COUNT

os.environ["LIANGMAI_TOKEN"] = "your_token"
client = Client()

# AI Agent 自动发现全部接口
functions = [
    {"name": m, "description": getattr(client, m).__doc__ or ""}
    for m in dir(client) if not m.startswith("_")
]
print(f"可用函数: {len(functions)}")  # 105

# 调用任意接口
result = client.stock_realtime(ts_code="000001")
```

## 获取 Token

访问 [liangmai.pro](https://liangmai.pro) 注册并获取 API Token。

## 相关链接

| 链接 | 地址 |
|------|------|
| 🌐 量脉平台 | [https://liangmai.pro](https://liangmai.pro) |
| 📦 PyPI 包 | [https://pypi.org/project/liangmai/](https://pypi.org/project/liangmai/) |
| 💻 GitHub | [https://github.com/liangmai-sdk/liangmai](https://github.com/liangmai-sdk/liangmai) |
| 🐛 问题反馈 | [https://github.com/liangmai-sdk/liangmai/issues](https://github.com/liangmai-sdk/liangmai/issues) |

## 许可证

MIT License © 2026 liangmai