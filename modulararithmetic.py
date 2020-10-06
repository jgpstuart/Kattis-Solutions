n, t = [int(x) for x in input().split()]

def eua(a,b):
        if a == 0:
                return b,0,1
        gcd, x, y = eua(b%a, a)
        return gcd, y-(b//a) *x, x


def operations(a, b, op, n):
    if op == "+":
        return(a+b)%n
    if op == "-":
        return(a-b)%n
    if op == "*":
        return(a*b)%n
    if op == "/":
        gcd, x, y = eua(b,n)
        if gcd != 1:
            return -1
        else:
            return x % n
        

while n != 0 and t != 0:
    for i in range(t):
        a, op, b = [x for x in input().split()]
        a = int(a)
        b = int(b)
        print(operations(a,b,op,n))
