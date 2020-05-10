seatsleft, weeksleft = [int(x) for x in input().split()]
week1 = [int(x) for x in input().split()]
checks = week1[0]

w1price = 0
pricesw1 = week1[1:checks+1]
ticketssold = week1[checks+1:]
profitw1 = []
for i in range(checks):
    if seatsleft >= ticketssold[i]:
        sell = ticketssold[i]
    else:
        sell = seatsleft
    
    profitw1.append([pricesw1[i] * sell, seatsleft - sell])

for i in range(weeksleft):
    week = [int(x) for x in input().split()]
    checks = week[0]
    prices = week[1:checks+1]
    ticketsold = week[checks+1:]
    profit = []
    for k in range(checks):
        profit.append(prices[k] * ticketsold[k])
    maxindex = profit.index(max(profit))
    
    for j in range(len(profitw1)):
        if profitw1[j][1] > 0:
            if (profitw1[j][1]) >= ticketsold[maxindex]:
                sell = ticketsold[maxindex]
            else:
                sell = profitw1[j][1]
            profitw1[j][0] = profitw1[j][0] + (prices[maxindex] * sell)
            profitw1[j][1] = profitw1[j][1] - sell

highprice = 0
indexwanted = 0
for i in range(len(profitw1)):
    if profitw1[i][0] == highprice:
        if pricesw1[indexwanted] > pricesw1[i]:
            indexwanted = i
            continue
    elif profitw1[i][0] > highprice:
        highprice = profitw1[i][0]
        indexwanted = i

print(highprice)
print(pricesw1[indexwanted])
