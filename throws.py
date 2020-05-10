children, total_throws = [int(x) for x in input().split()]
throws = [x for x in input().split()]
position = 0
previous = [0]
previous_number = 0

i = 0
while i < len(throws):
    if throws[i] != 'undo':
        number = int(throws[i])
        position = (position + (number % children)) % children
        previous.append(position)
        previous_number += 1
        i += 1
    else:
        i += 1
        previous_number -= int(throws[i])
        if previous_number < 0:
            previous_number = 0
        position = previous[previous_number]
        previous = previous[:previous_number+1]
        i += 1
print(position)