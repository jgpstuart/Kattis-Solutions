kth, nth = [int(x) for x in input().split()]
answer = ""

def batmanacci(n):
    if n  == 1:
        return "N"
    elif n == 2:
        return "A"
    else:
        return batmanacci(n-2) + batmanacci(n-1)

toprint = batmanacci(nth)

print(toprint[kth-1])
