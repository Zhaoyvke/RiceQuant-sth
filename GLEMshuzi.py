# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。
import pandas as pd
import numpy as np
import datetime
import math
# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    scheduler.run_weekly(rebalance,2)
# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    pass
def before_trading(context):
    num_stocks = 5
    fundamental_df = get_fundamentals(
        query(
            fundamentals.eod_derivative_indicator.pb_ratio,
            fundamentals.eod_derivative_indicator.pe_ratio,
        )
        .filter(
            fundamentals.eod_derivative_indicator.pe_ratio<15
        )
        .filter(
            fundamentals.eod_derivative_indicator.pb_ratio<1.5
        )
        .order_by(
            fundamentals.eod_derivative_indicator.market_cap.desc()
        ).limit(
            num_stocks
        )
    )
    context.fundamental_df = fundamental_df
    context.stocks = context.fundamental_df.columns.values

def rebalance(context,bar_dict):
    for stock in context.portfolio.positions:
        if stock not in context.fundamental_df:
            order_target_percent(stock, 0)
    weight = update_weights(context, context.stocks)
    for stock in context.fundamental_df:
        if weight != 0 and stock in context.fundamental_df:
            order_target_percent(stock,weight)
def update_weights(context,stocks):
    if len(stocks) == 0:
        return 0
    else:

        weight = .95/len(stocks)
        return weight
