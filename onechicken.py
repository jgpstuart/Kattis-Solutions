people, chicken = [int(x) for x in input().split()]

amount = chicken - people
if amount < 0:
    amount = amount * -1
    if amount == 1:
        amount = str(amount)
        print("Dr. Chaz needs " + amount + " more piece of chicken!")
    else:
        amount = str(amount)
        print("Dr. Chaz needs " + amount + " more pieces of chicken!")
elif amount == 1:
    amount = str(amount)
    print("Dr. Chaz will have " + amount + " piece of chicken left over!")
else:
    amount = str(amount)
    print("Dr. Chaz will have " + amount + " pieces of chicken left over!")
