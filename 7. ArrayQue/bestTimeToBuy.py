def maxProfit(prices):

# float -> Positive in Infinity
    min_Price = float('inf')
    max_profit = 0

    for p in prices:
        if p < min_Price:
            min_Price = p

                # sp - bp
        profit = p - min_Price

        if profit > max_profit:
            max_profit = profit


    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
