n, h, v = [int(x) for x in input().split()]
hPrime = n-h
vPrime = n-v

height = h if h > hPrime else hPrime
length = v if v > vPrime else vPrime

print(height * length * 4)
