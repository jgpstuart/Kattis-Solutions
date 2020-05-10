scoreboard = {}

players, threshhold, shots = [int(x) for x in input().split()]

# add players to the dictionary
for i in range(players):
    player = input()
    scoreboard[player] = 0

# shots loop
for i in range(shots):
    player, points = [x for x in input().split()]
    
    # add points to player
    scoreboard[player] += int(points)
    
    # check to see if player has reached the threshhold,
    # if yes, print message and remove from dictionary
    if scoreboard[player] >= threshhold:
        print(player + " wins!")
        scoreboard.pop(player)

# if no one was removed from the dictionary, print "No winner!"
if (len(scoreboard) == players):
    print("No winner!")
