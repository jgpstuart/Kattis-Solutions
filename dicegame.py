gunnar = [int(x) for x in input().split()]
emma = [int(x) for x in input().split()]

if sum(gunnar)/len(gunnar) > sum(emma) / len(emma):
    print("Gunnar")
elif sum(gunnar)/len(gunnar) == sum(emma) / len(emma):
    print("Tie")
else:
    print("Emma")
