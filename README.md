<p align="center">
  <h1 align="center">量脉金融数据平台 Liangmai</h1>
  <h4 align="center">Python SDK — 105个金融数据API，覆盖A股/指数/基金/龙虎榜/游资/早盘竞价</h4>
</p>

<p align="center">
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/v/liangmai?label=PyPI&color=blue" alt="PyPI"></a>
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/pyversions/liangmai" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
</p>

---

## 快速入门

### 安装

```bash
pip install liangmai
```

> 要求 Python >= 3.8。仅依赖 `requests`，零额外负担。

### 快速开始

```python
from liangmai import Client

client = Client(token="your_platform_token")

# 获取沪深京股票列表
stocks = client.stock_list()

# 查询实时行情
realtime = client.stock_realtime(ts_code="601012")

# 查询涨停股池
limit_up = client.pool_limit_up(trade_date="2025-06-26")

# 查询历史日线 K 线（前复权，100 条）
bars = client.quote_bars_history(full_code="000001.SZ", interval="d", cq="n", lt=100)
```

### 配置

支持两种方式传入 Token：

```python
# 方式一：构造参数
client = Client(token="your_token")

# 方式二：环境变量（推荐，12-Factor App 友好）
import os
os.environ["LIANGMAI_TOKEN"] = "your_token"
client = Client()  # 自动读取环境变量
```

环境变量列表：

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `LIANGMAI_TOKEN` | 平台 Token（必填） | — |
| `LIANGMAI_BASE_URL` | 网关地址（选填） | `https://liangmai.pro/api/gateway` |

```bash
# Linux / macOS
export LIANGMAI_TOKEN=your_platform_token

# Windows PowerShell
$env:LIANGMAI_TOKEN="your_platform_token"
```

### 错误处理

```python
try:
    client = Client(token="your_token")
    data = client.stock_realtime(ts_code="000001")
except RuntimeError as e:
    print(f"请求失败: {e}")
```

常见错误码：

| 错误 | 含义 | 解决 |
|------|------|------|
| `code=422` | 参数缺失或不合法 | 检查参数名和格式 |
| `code=403` | Token 无效或无权限 | 确认 Token 正确，且接口已开通 |
| `code=429` | 请求频率超限 | 降低调用频率 |
| `code=500` | 服务器内部错误（自动重试） | SDK 已内置自动重试 |

---

## 为什么选择量脉

量脉是一个**企业级金融数据平台**，为量化交易、金融分析、AI 投资决策提供底层数据支撑。

| 能力 | 详情 |
|------|------|
| 📊 **数据广度** | 沪深京 A 股 5000+ 标的、2000+ 指数、300+ ETF、全部板块与概念 |
| 🚀 **响应速度** | 毫秒级实时行情推送，历史数据秒级返回 |
| 🔄 **数据一致性** | 多源数据融合+自动校验，杜绝脏数据 |
| 🛡️ **高可用** | 多节点部署，99.9% 可用性 SLA |
| 🤖 **AI 就绪** | 标准 RESTful API，Token 鉴权，为 AI Agent 调用而生 |
| 📦 **开箱即用** | 官方 Python SDK 封装全部接口，`pip install` 一行即可 |

### 平台数据覆盖

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

---

## 接口参考（105 个）

> 以下所有接口通过 `client.方法名(参数)` 调用，返回 `{"code":0, "msg":"success", "data":[...]}` 格式。

### 📋 列表与日历（13）

获取基础股票列表、指数树、板块信息。

```python
stocks      = client.stock_list()           # 沪深京股票合并列表（推荐）
stocks_main = client.hs_list_main()         # 沪深A股基础列表
ipo         = client.ipo_calendar()         # 新股日历（按申购日期倒序）
tree        = client.sector_tree()          # 指数/行业/概念树
members     = client.sector_constituents(sector_code="sw1_01")   # 按板块查成分
sectors     = client.stock_sectors(ts_code="000001")             # 股票所属板块
indices     = client.index_list_main()      # 沪深主要指数列表
bj          = client.bj_list_stocks()       # 京市股票列表
bj_idx      = client.bj_list_indices()      # 京市指数列表
hk          = client.hk_list_stocks()       # 港股列表
kc          = client.kc_list_stocks()       # 科创板列表
funds       = client.fund_list_all()        # 沪深基金列表
etf         = client.fund_list_etf()        # ETF基金列表
```

### 📊 股池（5）

按交易日获取涨停、跌停、强势、次新、炸板股票池。

```python
limit_up    = client.pool_limit_up(trade_date="2025-06-26")    # 涨停股池
limit_down  = client.pool_limit_down(trade_date="2025-06-26")  # 跌停股池
strong      = client.pool_strong(trade_date="2025-06-26")      # 强势股池
subnew      = client.pool_subnew(trade_date="2025-06-26")      # 次新股池
broken      = client.pool_broken_board(trade_date="2025-06-26") # 炸板股池
```

### 🏢 公司资料（16）

查询单只股票的详细基本面信息，传 `ts_code` / `code` / `symbol` 三者之一即可。

```python
profile       = client.company_profile(ts_code="000001")           # 公司简介
index_member  = client.company_index_membership(ts_code="000001")  # 所属指数
exec_history  = client.company_exec_history(code="000001")         # 历届高管
board_history = client.company_board_history(symbol="000001")      # 历届董事会
supervisor    = client.company_supervisor_history(ts_code="000001")# 历届监事会
dividend      = client.company_dividend(ts_code="000001")          # 近年分红
seo           = client.company_seo(ts_code="000001")               # 近年增发
unlock        = client.company_unlock(ts_code="000001")            # 解禁限售
quarter_profit= client.company_quarter_profit(ts_code="000001")    # 季度利润
quarter_cash  = client.company_quarter_cashflow(ts_code="000001")  # 季度现金流
forecast      = client.company_forecast(ts_code="000001")          # 业绩预告
finance       = client.company_finance_metrics(ts_code="000001")   # 财务指标
holders_10    = client.company_holders_top10(ts_code="000001")     # 十大股东
float_10      = client.company_float_holders_top10(ts_code="000001") # 十大流通股东
holder_trend  = client.company_holder_trend(ts_code="000001")      # 股东户数变化
fund_hold     = client.company_fund_holdings(ts_code="000001")     # 基金持股
```

### 📈 实时行情与逐笔（6）

获取即时行情数据和当日交易明细。

```python
realtime    = client.stock_realtime(ts_code="601012")                           # 单股实时行情
ticks       = client.stock_ticks_today(ts_code="601012")                        # 当日逐笔成交
multi       = client.stock_realtime_multi(stock_codes="000001,600519,300750")   # 多股实时（≤20只）
broker_rt   = client.quote_realtime_broker(ts_code="601012")                    # 专业行情源实时
broker_5    = client.quote_five_broker(ts_code="601012")                        # 买卖五档
flow_hist   = client.capital_flow_history(ts_code="601012", st="20250601", et="20250626")
```

### 🕯️ K线/分时（5）

获取股票的 K 线数据（最新/历史）、涨跌停价、行情指标、基础信息。

```python
bars_latest = client.quote_bars_latest(
    full_code="000001.SZ", interval="d", cq="n", lt=5
)  # 最新K线（lt≤5，日线/前复权）

bars_history = client.quote_bars_history(
    full_code="000001.SZ", interval="d", cq="n", lt=100,
    st="20250101", et="20250626"
)  # 历史K线

stop_prices = client.quote_stop_prices(full_code="000001.SZ")              # 历史涨跌停价
indicators  = client.quote_market_indicators(full_code="000001.SZ")        # 行情指标
instrument  = client.stock_instrument(full_code="000001.SZ")               # 股票基础信息
```

> **参数说明**：`interval` 周期 `1`/`5`/`15`/`30`/`60`/`d`/`w`/`m`/`y`；`cq` 复权 `n`前复权 `b`后复权 `s`不复权；K线 `st`/`et` 格式 `YYYYMMDD` 或 `YYYYMMDDhhmmss`

### 📑 财务报表（8）

查询三大报表、财务指标、股东结构等。

```python
balance     = client.fin_balance_sheet(full_code="000001.SZ")              # 资产负债表
income      = client.fin_income_statement(full_code="000001.SZ")           # 利润表
cashflow    = client.fin_cashflow_statement(full_code="000001.SZ")         # 现金流量表
per_share   = client.fin_per_share_index(full_code="000001.SZ")            # 财务主要指标
capital     = client.fin_capital_structure(full_code="000001.SZ")          # 股本结构
top10       = client.fin_top10_holders(full_code="000001.SZ")              # 十大股东
float_top10 = client.fin_top10_float_holders(full_code="000001.SZ")        # 十大流通股东
holder_cnt  = client.fin_holder_counts(full_code="000001.SZ")              # 股东户数
```

> 可选参数 `st`/`et` 限定日期范围

### 🔬 技术指标（5）

```python
macd  = client.tech_macd(full_code="000001.SZ", interval="d", cq="n")   # MACD
ma    = client.tech_ma(full_code="000001.SZ", interval="d", cq="n")     # 均线
boll  = client.tech_boll(full_code="000001.SZ", interval="d", cq="n")   # BOLL
kdj   = client.tech_kdj(full_code="000001.SZ", interval="d", cq="n")    # KDJ
ma_old= client.stock_ma(ts_code="000001", period="5m")                  # 简易均线（旧版）
```

### 📉 指数（8）

指数实时行情、K线和技术指标。

```python
idx_rt    = client.index_realtime_broker(index_code="000001.SH")        # 指数实时
idx_latest= client.index_bars_latest(index_full="000001.SH", interval="d") # 指数最新K线
idx_hist  = client.index_bars_history(index_full="000001.SH", interval="d") # 指数历史K线
idx_macd  = client.index_tech_macd(index_code="000001.SH")              # 指数MACD
idx_ma    = client.index_tech_ma(index_code="000001.SH")                # 指数MA
idx_boll  = client.index_tech_boll(index_code="000001.SH")              # 指数BOLL
idx_kdj   = client.index_tech_kdj(index_code="000001.SH")               # 指数KDJ
```

### 🌏 京市/港股/科创板/基金实时（7）

```python
bj_rt   = client.bj_quote_realtime(ts_code="830799")     # 京市实时
bj_five = client.bj_quote_five(ts_code="830799")         # 京市五档
hk_rt   = client.hk_quote_realtime(ts_code="00700")      # 港股实时
hk_five = client.hk_quote_five(ts_code="00700")          # 港股五档
kc_rt   = client.kc_quote_realtime(ts_code="688981")     # 科创实时
kc_five = client.kc_quote_five(ts_code="688981")         # 科创五档
fd_rt   = client.fund_quote_realtime(ts_code="510050")   # 基金实时
```

### 🌐 全市场实时（1）

```python
all_market = client.market_realtime_all_network()  # 全市场实时快照（高阶套餐，限频）
```

### 🐉 龙虎榜与游资（5）

```python
dragon    = client.dragon_tiger(date="2025-06-26")            # 龙虎榜查询
youzi_all = client.youzi_all(date="2025-06-26")               # 全部游资上榜
youzi_one = client.youzi_by_name(yzmc="炒股养家", date="2025-06-26") # 按游资名称查询
youzi_gegu= client.youzi_gegu(code="000001", start_date="2025-06-01", end_date="2025-06-26")
youzi_names = client.youzi_name()                             # 游资名称列表
```

### 🧨 早盘竞价（13）

竞价热点板块、抢筹排序。

```python
# 热点板块竞价
bkjj       = client.base_bkjj(start_date="2025-06-26", end_date="2025-06-26", type_="1")
bkjjzq     = client.base_bkjjzq(trade_date="2025-06-26")               # 增强版
bkjj_stocks= client.base_zqbk_code_list(trade_date="2025-06-26", bk_code="BK0001")
bk_stocks  = client.base_bk_code_list(start_date="2025-06-26", end_date="2025-06-26", bk_code="BK0001")

# 早盘抢筹
jjqc       = client.base_jjqc(trade_date="2025-06-26", period="1", type_="1")  # 委托金额
jjqc_amt   = client.base_jjqc_cje(trade_date="2025-06-26", period="1")          # 成交金额
jjqc_open  = client.base_jjqc_open(trade_date="2025-06-26", period="1")         # 开盘金额
jjqc_zf    = client.base_jjqc_zf(trade_date="2025-06-26", period="1")           # 涨幅排序

# 尾盘抢筹
tail_wt    = client.base_jjqc_tail_wt(trade_date="2025-06-26")          # 委托金额
tail_cje   = client.base_jjqc_tail_cje(trade_date="2025-06-26")         # 成交金额
tail_close = client.base_jjqc_tail_close(trade_date="2025-06-26")       # 收盘金额
tail_zf    = client.base_jjqc_tail_zf(trade_date="2025-06-26")          # 涨幅排序

# 竞价一字板
yizi       = client.jjyizi_list(trade_date="2025-06-26")
```

### 🔧 基础数据（4）

```python
stocks_st     = client.base_st()                    # ST股票列表
concept_codes = client.base_gn()                    # 概念代码列表
sector_codes  = client.base_bk()                    # 板块代码列表
emotion       = client.base_emotional_cycle()       # 情绪周期
```

### 💸 板块资金流与成分（3）

```python
bk_flow  = client.base_bk_flow_history(bk_code="BK0001")                    # 板块资金流
bk_list  = client.base_bk_list(bk_code="BK0001", page_no=1, page_size=20)   # 板块成分股
code_flow= client.base_code_flow(code="000001", start_date="2025-06-01",
           end_date="2025-06-26", page_no=1, page_size=50)                  # 个股资金流向
```

### ⚡ 异动数据（3）

```python
all_changes = client.change_all_history(start_date="2025-06-01", end_date="2025-06-26", type_="1")
code_change = client.change_code_history(code="000001", start_date="2025-06-01", end_date="2025-06-26")
hot_rank    = client.change_ren_qi()                                        # 人气排行
```

### 🛡️ 风险监控（4）

```python
reduce  = client.alarm_data(trade_date="2025-06-26", type_="1")             # 大股东减持
unlock  = client.alarm_data_unlock(trade_date="2025-06-26", type_="1")      # 大比例解禁
risk    = client.alarm_data_risk(trade_date="2025-06-26", type_="1")        # 风险监控
serious = client.alarm_data_serious(trade_date="2025-06-26", type_="1")     # 严重异动
```

> 以上 `type_`、`start_date`、`end_date` 等具体值请参考平台文档 [liangmai.pro/docs](https://liangmai.pro/docs)

---

## SDK 工程设计

```python
from liangmai import Client, API_COUNT, call
# API_COUNT = 105  ← 导入即知接口总数

client = Client(
    token="your_token",
    timeout=30,  # 请求超时（秒）
)
```

| 特性 | 说明 |
|------|------|
| 🔄 **自动重试** | 5xx / code=500 自动重试，与平台文档页行为一致 |
| 🏷️ **参数别名** | `ts_code` / `code` / `symbol` 均可，`trade_date` / `date` 混用 |
| 📝 **市场后缀补全** | 6 位代码自动推断 `.SZ` / `.SH` / `.BJ` |
| 🔧 **环境变量驱动** | `LIANGMAI_TOKEN` + `LIANGMAI_BASE_URL` 配置 |
| 📦 **零臃肿** | 仅依赖 `requests`，不引入 pandas/numpy |
| 🐍 **全版本** | Python 3.8 ~ 3.14 全面支持 |
| 🤖 **AI 友好** | 标准类型注解 + docstring，AI Agent 可直接调用 |

### AI Agent 调用示例

```python
from liangmai import Client

client = Client(token="your_token")

# AI Agent 自动发现全部 105 个接口
functions = [
    {"name": m, "description": getattr(client, m).__doc__ or ""}
    for m in dir(client) if not m.startswith("_")
]

# 调用任意接口
result = client.stock_realtime(ts_code="000001")
```

---

## 获取 Token

访问 [liangmai.pro](https://liangmai.pro) 注册并获取 API Token。

## 相关链接

| 链接 | 地址 |
|------|------|
| 🌐 量脉平台 | [https://liangmai.pro](https://liangmai.pro) |
| 📦 PyPI | [https://pypi.org/project/liangmai/](https://pypi.org/project/liangmai/) |
| 💻 GitHub | [https://github.com/liangmai-sdk/liangmai](https://github.com/liangmai-sdk/liangmai) |
| 🐛 问题反馈 | [https://github.com/liangmai-sdk/liangmai/issues](https://github.com/liangmai-sdk/liangmai/issues) |

## 许可证

MIT License © 2026 liangmai