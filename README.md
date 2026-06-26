<p align="center">
  <h1 align="center">量脉 · 金融数据平台</h1>
  <h4 align="center">官方 Python SDK · 105 个金融数据 API</h4>
</p>

<p align="center">
  <a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/v/liangmai?label=PyPI&color=blue" alt="PyPI"></a>
a href="https://pypi.org/project/liangmai/"><img src="https://img.shields.io/pypi/pyversions/liangmai" alt="Python"></a>
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

## 接口全览（105 个）

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