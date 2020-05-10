cost = float(input())
lawns = int(input())
answer = 0.00000000

for i in range(lawns):
    x,y = [float(x) for x in input().split()]
    area = x * y
    answer += area * cost
print(answer)
