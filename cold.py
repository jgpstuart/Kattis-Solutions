days = int(input())
answer = 0
[*queue] = [int(x) for x in input().split()]
for i in range(days):
    if queue[i] < 0:
        answer += 1
print(answer)
        
