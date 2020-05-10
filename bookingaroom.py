total_rooms, booked = [int(x) for x in input().split()]
rooms = []

for i in range(1, total_rooms + 1):
    rooms.append(int(i))

for j in range(booked):
    rooms.remove(int(input()))

if len(rooms) == 0:
    print("too late")
else:
    print(rooms[0])
