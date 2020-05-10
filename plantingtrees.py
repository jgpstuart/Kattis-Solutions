trees = int(input())
day = 1
seedlings = [int(x) for x in input().split()]
checker = []

seedlings.sort(reverse = True)
for i in range(len(seedlings)):
    checker.append(seedlings[i] + i)
answer = max(checker) + 2
print(answer)
