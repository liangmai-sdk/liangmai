<p align="center">
  <h1 align="center">量脉金融数据平台 Liangmai</h1>
  <h4 align="center">Python SDK — 105个金融数据API，覆盖A股/指数/基金/龙虎榜/游资/早盘竞价</h4>
</p>

<p align="center">
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/v/liangmai?label=PyPI&color=blue" alt="PyPI"></a>
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/pyversions/liangmai" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
</p>

## 什么是量脉

量脉（Liangmai）是一个**企业级金融数据平台**，提供沪深京 A 股、指数、基金、港股、科创板、京市、龙虎榜、游资上榜、早盘竞价、板块资金流、异动监控等全线金融数据接口。量脉平台为量化交易、金融分析、AI 投资决策、股票研究、财经数据挖掘提供底层数据支撑。

本 SDK 是量脉平台的官方 Python 客户端，封装平台**全部 105 个金融数据 API**。无论是量化策略回测、股票实时监控、财务数据分析还是龙虎榜追踪，`pip install liangmai` 一行命令即可接入。

**适合场景**：量化交易系统、AI Agent 金融助手、股票分析工具、财经数据看板、回测框架、金融数据 ETL。

**关键词**：`Python 金融数据 SDK` `A股数据接口` `股票行情API` `龙虎榜数据` `游资查询` `财务数据` `K线数据` `指数数据` `早盘竞价` `量化交易` `金融Python库` `沪深股票` `港股数据` `科创板数据` `板块资金流` `异动监控` `风险预警`

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

```python
# 方式一：构造参数
client = Client(token="your_token")

# 方式二：环境变量（推荐，12-Factor 友好）
import os
os.environ["LIANGMAI_TOKEN"] = "your_token"
client = Client()  # 自动读取
```

| 环境变量 | 说明 | 默认值 |
|----------|------|--------|
| `LIANGMAI_TOKEN` | 平台 Token（必填） | — |
| `LIANGMAI_BASE_URL` | 网关地址（选填） | `https://liangmai.pro/api/gateway` |

### 错误处理

```python
try:
    client = Client(token="your_token")
    data = client.stock_realtime(ts_code="000001")
except RuntimeError as e:
    print(f"请求失败: {e}")
```

| 错误码 | 含义 | 解决 |
|--------|------|------|
| `code=422` | 参数缺失 | 检查参数名和格式 |
| `code=403` | Token 无效 | 确认 Token 正确且接口已开通 |
| `code=429` | 频率超限 | 降低调用频率 |
| `code=500` | 服务器错误（自动重试） | SDK 内置自动重试 |

---

## 为什么选择量脉

| 能力 | 详情 |
|------|------|
| 📊 数据广度 | 沪深京 A 股 5000+ 标的、2000+ 指数、300+ ETF、全部板块与概念 |
| 🚀 响应速度 | 毫秒级实时行情推送，历史数据秒级返回 |
| 🔄 数据质量 | 多源融合+自动校验，杜绝脏数据 |
| 🛡️ 高可用 | 多节点部署，99.9% SLA |
| 🤖 AI 就绪 | 标准 REST API，Token 鉴权，专为 AI Agent 调用设计 |
| 📦 开箱即用 | 官方 Python SDK 封装全部接口 |

### 数据覆盖矩阵

```
📈 沪深A股    5000+ 标的  实时行情/K线/逐笔/资金流/财务
📊 指数        2000+ 标的  实时/K线/MACD/MA/BOLL/KDJ
🏦 科创板/京市  全量覆盖  实时行情/五档买卖
🇭🇰 港股        全量覆盖  实时行情/五档买卖
💰 基金/ETF     300+ 标的  实时行情
🐉 龙虎榜       全量历史  上榜明细/游资追踪
🧨 早盘竞价     实时推送  热点板块/抢筹排序/一字板
⚡ 异动监控     实时推送  全量异动/个股异动/人气排行
🛡️ 风险预警     实时推送  减持/解禁/严重异动
```

---

## 接口参考（105 个金融数据 API）

> 以下所有接口通过 `client.方法名(参数)` 调用，返回 `{"code":0, "msg":"success", "data":[...]}` 格式。

### 📋 列表与日历（13）
获取基础股票列表、指数树、板块信息。

```python
client.stock_list()                         # 沪深京股票合并列表（推荐）
client.hs_list_main()                       # 沪深A股基础列表
client.ipo_calendar()                       # 新股日历（按申购日期倒序）
client.sector_tree()                        # 指数/行业/概念树
client.sector_constituents(sector_code="sw1_01")  # 按板块查成分
client.stock_sectors(ts_code="000001")      # 股票所属板块
client.index_list_main()                    # 沪深主要指数列表
client.bj_list_stocks()                     # 京市股票列表
client.bj_list_indices()                    # 京市指数列表
client.hk_list_stocks()                     # 港股列表
client.kc_list_stocks()                     # 科创板列表
client.fund_list_all()                      # 沪深基金列表
client.fund_list_etf()                      # ETF基金列表
```

### 📊 股池（5）
按交易日获取涨停、跌停、强势、次新、炸板股票池。

```python
client.pool_limit_up(trade_date="2025-06-26")      # 涨停股池
client.pool_limit_down(trade_date="2025-06-26")    # 跌停股池
client.pool_strong(trade_date="2025-06-26")        # 强势股池
client.pool_subnew(trade_date="2025-06-26")        # 次新股池
client.pool_broken_board(trade_date="2025-06-26")  # 炸板股池
```

### 🏢 公司资料（16）
查询单只股票的详细基本面信息。`ts_code` / `code` / `symbol` 三者传一即可。

```python
client.company_profile(ts_code="000001")           # 公司简介
client.company_index_membership(ts_code="000001")  # 所属指数
client.company_exec_history(code="000001")         # 历届高管
client.company_board_history(symbol="000001")      # 历届董事会
client.company_supervisor_history(ts_code="000001")# 历届监事会
client.company_dividend(ts_code="000001")          # 近年分红
client.company_seo(ts_code="000001")               # 近年增发
client.company_unlock(ts_code="000001")            # 解禁限售
client.company_quarter_profit(ts_code="000001")    # 季度利润
client.company_quarter_cashflow(ts_code="000001")  # 季度现金流
client.company_forecast(ts_code="000001")          # 业绩预告
client.company_finance_metrics(ts_code="000001")   # 财务指标
client.company_holders_top10(ts_code="000001")     # 十大股东
client.company_float_holders_top10(ts_code="000001")  # 十大流通股东
client.company_holder_trend(ts_code="000001")      # 股东户数变化
client.company_fund_holdings(ts_code="000001")     # 基金持股
```

### 📈 实时行情与逐笔（6）
获取即时行情数据和当日交易明细。

```python
client.stock_realtime(ts_code="601012")            # 单股实时行情
client.stock_ticks_today(ts_code="601012")         # 当日逐笔成交
client.stock_realtime_multi(stock_codes="000001,600519,300750")  # 多股（≤20只）
client.quote_realtime_broker(ts_code="601012")     # 专业行情源实时
client.quote_five_broker(ts_code="601012")         # 买卖五档
client.capital_flow_history(ts_code="601012", st="20250601", et="20250626")
```

### 🕯️ K线/分时（5）
获取 K 线、涨跌停价、行情指标、基础信息。`interval` 支持 `1/5/15/30/60/d/w/m/y`，`cq` 复权方式 `n`前复权/`b`后复权/`s`不复权。

```python
client.quote_bars_latest(full_code="000001.SZ", interval="d", cq="n", lt=5)
client.quote_bars_history(full_code="000001.SZ", interval="d", cq="n", lt=100, st="20250101", et="20250626")
client.quote_stop_prices(full_code="000001.SZ")
client.quote_market_indicators(full_code="000001.SZ")
client.stock_instrument(full_code="000001.SZ")
```

> K线 `st`/`et` 格式 `YYYYMMDD` 或 `YYYYMMDDhhmmss`；最新 K 线 `lt` 最多 5 条。

### 📑 财务报表（8）
智能获取三大报表、财务指标、股东结构。支持可选参数 `st`/`et` 限定日期。

```python
client.fin_balance_sheet(full_code="000001.SZ")          # 资产负债表
client.fin_income_statement(full_code="000001.SZ")       # 利润表
client.fin_cashflow_statement(full_code="000001.SZ")     # 现金流量表
client.fin_per_share_index(full_code="000001.SZ")        # 财务主要指标
client.fin_capital_structure(full_code="000001.SZ")      # 股本结构
client.fin_top10_holders(full_code="000001.SZ")          # 十大股东（财报口径）
client.fin_top10_float_holders(full_code="000001.SZ")    # 十大流通股东（财报口径）
client.fin_holder_counts(full_code="000001.SZ")          # 股东户数
```

### 🔬 技术指标（5）

```python
client.tech_macd(full_code="000001.SZ", interval="d", cq="n")  # MACD
client.tech_ma(full_code="000001.SZ", interval="d", cq="n")    # 均线
client.tech_boll(full_code="000001.SZ", interval="d", cq="n")  # BOLL
client.tech_kdj(full_code="000001.SZ", interval="d", cq="n")   # KDJ
client.stock_ma(ts_code="000001", period="5m")                 # 简易均线
```

### 📉 指数（8）
指数实时行情、K线及 MACD/MA/BOLL/KDJ 技术指标。

```python
client.index_realtime_broker(index_code="000001.SH")           # 指数实时
client.index_bars_latest(index_full="000001.SH", interval="d") # 指数最新K线
client.index_bars_history(index_full="000001.SH", interval="d")# 指数历史K线
client.index_tech_macd(index_code="000001.SH")                 # 指数MACD
client.index_tech_ma(index_code="000001.SH")                   # 指数MA
client.index_tech_boll(index_code="000001.SH")                 # 指数BOLL
client.index_tech_kdj(index_code="000001.SH")                  # 指数KDJ
```

### 🌏 京市/港股/科创板/基金实时（7）

```python
client.bj_quote_realtime(ts_code="830799")    # 京市实时
client.bj_quote_five(ts_code="830799")        # 京市五档
client.hk_quote_realtime(ts_code="00700")     # 港股实时
client.hk_quote_five(ts_code="00700")         # 港股五档
client.kc_quote_realtime(ts_code="688981")    # 科创实时
client.kc_quote_five(ts_code="688981")        # 科创五档
client.fund_quote_realtime(ts_code="510050")  # 基金实时
```

### 🌐 全市场实时（1）

```python
client.market_realtime_all_network()  # 全市场实时快照（高阶套餐）
```

### 🐉 龙虎榜与游资（5）

```python
client.dragon_tiger(date="2025-06-26")                           # 龙虎榜查询
client.youzi_all(date="2025-06-26")                              # 全部游资上榜
client.youzi_by_name(yzmc="炒股养家", date="2025-06-26")          # 按游资名称
client.youzi_gegu(code="000001", start_date="2025-06-01", end_date="2025-06-26")
client.youzi_name()                                               # 游资名称列表
```

### 🧨 早盘竞价（13）
竞价热点板块、早盘抢筹（委托/成交/开盘/涨幅）排序、尾盘抢筹、竞价一字板。

```python
# 热点板块竞价
client.base_bkjj(start_date="2025-06-26", end_date="2025-06-26", type_="1")
client.base_bkjjzq(trade_date="2025-06-26")
client.base_zqbk_code_list(trade_date="2025-06-26", bk_code="BK0001")
client.base_bk_code_list(start_date="2025-06-26", end_date="2025-06-26", bk_code="BK0001")

# 早盘抢筹
client.base_jjqc(trade_date="2025-06-26", period="1", type_="1")   # 委托金额
client.base_jjqc_cje(trade_date="2025-06-26", period="1")           # 成交金额
client.base_jjqc_open(trade_date="2025-06-26", period="1")          # 开盘金额
client.base_jjqc_zf(trade_date="2025-06-26", period="1")            # 涨幅排序

# 尾盘抢筹
client.base_jjqc_tail_wt(trade_date="2025-06-26")    # 委托金额
client.base_jjqc_tail_cje(trade_date="2025-06-26")   # 成交金额
client.base_jjqc_tail_close(trade_date="2025-06-26") # 收盘金额
client.base_jjqc_tail_zf(trade_date="2025-06-26")    # 涨幅排序

# 竞价一字板
client.jjyizi_list(trade_date="2025-06-26")
```

### 🔧 基础数据（4）

```python
client.base_st()                    # ST股票列表
client.base_gn()                    # 概念代码列表
client.base_bk()                    # 板块代码列表
client.base_emotional_cycle()       # 情绪周期
```

### 💸 板块资金流与成分（3）

```python
client.base_bk_flow_history(bk_code="BK0001")
client.base_bk_list(bk_code="BK0001", page_no=1, page_size=20)
client.base_code_flow(code="000001", start_date="2025-06-01", end_date="2025-06-26", page_no=1, page_size=50)
```

### ⚡ 异动数据（3）

```python
client.change_all_history(start_date="2025-06-01", end_date="2025-06-26", type_="1")
client.change_code_history(code="000001", start_date="2025-06-01", end_date="2025-06-26")
client.change_ren_qi()    # 人气排行
```

### 🛡️ 风险监控（4）

```python
client.alarm_data(trade_date="2025-06-26", type_="1")          # 大股东减持
client.alarm_data_unlock(trade_date="2025-06-26", type_="1")   # 大比例解禁
client.alarm_data_risk(trade_date="2025-06-26", type_="1")     # 风险监控
client.alarm_data_serious(trade_date="2025-06-26", type_="1")  # 严重异动
```

> 参数具体值请参考平台文档 [liangmai.pro/docs](https://liangmai.pro/docs)

---

## SDK 工程设计

```python
from liangmai import Client, API_COUNT, call
# API_COUNT = 105  ← 导入即知接口总数

client = Client(token="your_token", timeout=30)
```

| 特性 | 说明 |
|------|------|
| 🔄 自动重试 | 5xx / code=500 自动重试，与平台文档页一致 |
| 🏷️ 参数别名 | `ts_code`/`code`/`symbol` 均可，`trade_date`/`date` 混用 |
| 📝 市场后缀自动补全 | 6位代码自动推断 `.SZ`/`.SH`/`.BJ` |
| 🔧 环境变量驱动 | `LIANGMAI_TOKEN` + `LIANGMAI_BASE_URL` |
| 📦 零臃肿 | 仅依赖 `requests`，不引入 pandas/numpy |
| 🐍 全版本 | Python 3.8 ~ 3.14 全面支持 |
| 🤖 AI 友好 | 类型注解 + docstring，AI Agent 可直接调用 |

### AI Agent 调用示例

```python
from liangmai import Client

client = Client(token="your_token")

# AI Agent 自动发现 105 个接口
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