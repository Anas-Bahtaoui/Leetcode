def maxProfits(prices):

    if len(prices) == 0:
        return 0

    max_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit

#test cases

print(maxProfits([7,1,5,3,6,4]))

print(maxProfits([7,6,4,3,1]))

print(maxProfits([1,2]))

print(maxProfits([2,1,2,0,1]))

print(maxProfits([2,1,2,1,0,1,2]))