votes = []
vote_cast = input()
most_votes = 0
winnter = ""
votes_counted = []

while vote_cast != "***":
    votes.append(vote_cast)
    vote_cast = input()

temp = set(votes)
candidates = list(temp)

for i in range(len(candidates)):
    test = candidates[i]
    votes_counted.append(votes.count(test))
    if votes.count(test) > most_votes:
        most_votes = votes.count(test)
        winner = candidates[i]
    if i == len(candidates) -1:
        highest = max(votes_counted)
        if votes_counted.count(highest) == 1:
            print(winner)
        else:
            print("Runoff!")
