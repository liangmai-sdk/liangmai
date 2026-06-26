"""量脉 SDK 基础使用示例。

使用前请设置环境变量 LIANGMAI_TOKEN，或修改下方 TOKEN 变量。
"""

import os

from liangmai import Client

TOKEN = os.environ.get("LIANGMAI_TOKEN", "your_token_here")


def examples():
    client = Client(token=TOKEN)

    # 1) 股票列表
    print("=== 股票列表 ===")
    data = client.stock_list()
    print(f"code={data['code']}, count={len(data.get('data', []))}")
    if data["data"]:
        print(f"第一条: {data['data'][0]}")

    # 2) 实时行情
    print("\n=== 实时行情 (601012) ===")
    data = client.stock_realtime(ts_code="601012")
    print(data)

    # 3) 涨停股池
    print("\n=== 涨停股池 ===")
    data = client.pool_limit_up(trade_date="2025-04-01")
    print(f"code={data['code']}, count={len(data.get('data', []))}")

    # 4) 历史 K 线
    print("\n=== 历史 K 线 (000001.SZ 日线) ===")
    data = client.quote_bars_history(
        full_code="000001.SZ",
        interval="d",
        cq="n",
        lt=10,
    )
    print(f"code={data['code']}, bars={len(data.get('data', []))}")

    # 5) 指数实时行情
    print("\n=== 上证指数 ===")
    data = client.index_realtime(index_code="000001")
    print(data)


if __name__ == "__main__":
    examples()