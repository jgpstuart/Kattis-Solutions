n = int(input())
answer = 0

for i in range(n):
    temp = int(input())
    exponent = temp % 10
    temp = temp // 10
    answer += temp ** exponent
print(answer)
