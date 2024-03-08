# 生成式
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
list = [100, 102, 300, 40, 15]
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)
price3 = {key: value for key, value in prices.items() if value < 100}
print(price3)
prices4 = [value for value, value in prices.items() if value > 100]
print(prices4)
