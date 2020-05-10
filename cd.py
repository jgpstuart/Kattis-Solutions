from sys import stdin

N, M = [int(x) for x in input().split()]

while N != 0 and M !=0:
    jack = set()
    for i in range(N):
        jack.add(int(stdin.readline()))
    sell = 0
    for i in range(N):
        sell += int(stdin.readline()) in jack
    print(sell)
    N, M = [int(x) for x in input().split()]
