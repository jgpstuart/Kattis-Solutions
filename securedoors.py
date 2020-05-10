n = int(input())
inside = []


for i in range(n):
    check = []
    check += input().split()
    answer = []
    if check[0] == 'entry':
        if check[1] in inside:
            print(check[1] + " entered (ANOMALY)")
        else:
            inside.append(check[1])
            print(check[1] + " entered")
    elif check[0] == 'exit':
        if check[1] in inside:
            inside.remove(check[1])
            print(check[1] + " exited")
        else:
            print(check[1] + " exited (ANOMALY)")
            
