stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def totals_price(stock, prices):
    k = 0
    for stock, prices in zip(stock.values(), prices.values()):
        k += stock*prices
    return k
print(totals_price(stock, prices))