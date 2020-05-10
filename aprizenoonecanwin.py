items, minprice = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]
answers = prices.copy()

if len(prices) == 1:
    print("1")
else:
    for i in range(len(prices)):
        test = prices.pop(i)
        if test in answers:
            for j in range(len(prices)):
                    if test + prices[j] > minprice:
                        removeit = prices[j]
                        while removeit in answers:
                            answers.remove(removeit)
        prices.insert(i, test)
    print(len(answers))
