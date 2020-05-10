import heapq

cities, boxes = [int(x) for x in input().split()]
population = []
boxes_assigned = []
votes_per_box = []

while cities != -1 and boxes != -1:
    for i in range(cities):
        population.append(int(input()))
        boxes_assigned.append(1)
        votes_per_box.append(population[i])
        boxes -= 1

    while boxes != 0:
        max_votes = max(votes_per_box)
        index_max = votes_per_box.index(max_votes)
        boxes_assigned[index_max] += 1
        boxes -= 1
        for i in range(cities):
            votes_per_box[i] = population[i]/boxes_assigned[i]

    print(max(votes_per_box))

    empty = input()
    cities, boxes = [int(x) for x in input().split()]
    population = []
    boxes_assigned = []
    votes_per_box = []
