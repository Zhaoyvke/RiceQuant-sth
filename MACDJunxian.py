import talib

# 初始化函数
def init(context):
    context.s1 = "000001.XSHE"
    context.SHORTPERIOD = 12
    context.LONGPERIOD = 26
    context.SMOOTHPERIOD = 9
    context.OBSERVATION = 100
    context.introduction = 'I am the most lovel'

def handle_bar(context, bar_dict):
    prices = history_bars(context.s1, context.OBSERVATION, '1d', 'close')

    macd, signal, hist = talib.MACD(prices, context.SHORTPERIOD,context.LONGPERIOD, context.SMOOTHPERIOD)

    if macd[-1] - signal[-1] > 0 and macd[-2] - signal[-2] < 0:
        # 满仓入股
        order_target_percent(context.s1, 1)
        logger.info(context.introduction)

    if macd[-1] - signal[-1] < 0 and macd[-2] - signal[-2] > 0:
        # 获取该股票的仓位
        curPosition = context.portfolio.positions[context.s1].quantity
        # 清仓
        if curPosition > 0:
            order_target_value(context.s1, 0)
