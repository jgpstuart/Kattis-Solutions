tests = int(input())
power = 10**9+7

for i in range(tests):
    digits = int(input())
    answer = pow(8 * pow(9, digits-1, power), 1, power)
    print(answer)
