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
    for j in range(checks):
        for k in range(len(weeksleft)):
            
