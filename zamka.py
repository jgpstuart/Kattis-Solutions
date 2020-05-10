N = int(input())
M = int(input())
X = int(input())
numbertotal = 0
count = 0
answer = 0

for i in range(N,M+1):
    digittest = str(i)
    for j in range(len(digittest)):
        numbertotal += int(digittest[j])
    if numbertotal == X and count == 0:
        print(i)
        count += 1
    if numbertotal == X and count != 0:
        answer = i
    numbertotal = 0
print(answer)
