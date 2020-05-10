team1 = 0
team2 = 0
team3 = 0
team4 = 0
team5 = 0
s1, s2, s3, s4 = [int(x) for x in input().split()]
team1 = s1 + s2 + s3 + s4
s1, s2, s3, s4 = [int(x) for x in input().split()]
team2 = s1 + s2 + s3 + s4
s1, s2, s3, s4 = [int(x) for x in input().split()]
team3 = s1 + s2 + s3 + s4
s1, s2, s3, s4 = [int(x) for x in input().split()]
team4 = s1 + s2 + s3 + s4
s1, s2, s3, s4 = [int(x) for x in input().split()]
team5 = s1 + s2 + s3 + s4
if team1 > team2 and team1 > team3 and team1 > team4 and team1 > team5:
    print(1, team1)
elif team2 > team1 and team2 > team3 and team2 > team4 and team2 > team5:
    print(2, team2)
elif team3 > team1 and team3 > team2 and team3 > team4 and team3 > team5:
    print(3, team3)
elif team4 > team1 and team4 > team2 and team4 > team3 and team4 > team5:
    print(4, team4)
else:
    print(5, team5)
