cases = int(input())
count = 0

for i in range(0,cases):
    package = input()
    package = package.lower()
    if "pink" in package or "rose" in package:
        count += 1
if count == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(count)
    