start = 2
answer = 4

iterations = int(input())

for i in range(iterations):
    start += (start - 1)

answer = start ** 2

print(answer)
