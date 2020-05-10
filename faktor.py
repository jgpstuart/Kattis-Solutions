article, impact = [int(x) for x in input().split()]

answer = (article * (impact - 1)) + 1

print(answer)
