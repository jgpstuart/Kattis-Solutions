x, y, n = [int(x) for x in input().split()]
for i in range(1, n+1):
    answer = ''
    if i % x == 0:
        answer +="Fizz"
    if i % y == 0:
        answer +="Buzz"
    if i % x != 0 and i % y != 0:
        answer += str(i)
    print(answer)
