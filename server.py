tasks, runtime = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]
tasks_complete = 0

for i in range(tasks):
    runtime -= times[i]
    if runtime >= 0:
        tasks_complete += 1
    if runtime < 0:
        break

print(tasks_complete)
