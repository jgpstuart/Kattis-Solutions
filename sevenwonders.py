test = input()
t = []
g = []
c = []
answer = 0

for i in range(len(test)):
    if test[i] == "T":
        t.append(test[i])
    if test[i] == "G":
        g.append(test[i])
    if test[i] == "C":
        c.append(test[i])

answer = len(t) ** 2 + len(g) ** 2 + len(c) ** 2

tlen = len(t)
glen = len(g)
clen = len(c)

while tlen != 0 and glen != 0 and clen != 0:
    answer += 7
    tlen -= 1
    glen -= 1
    clen -= 1

print(answer)
