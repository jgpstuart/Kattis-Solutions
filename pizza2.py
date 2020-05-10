import math

R, C = [int(x) for x in input().split()]

cheese_radius = R-C

cheese  = math.pi * cheese_radius * cheese_radius
pizza = math.pi * R * R

print(cheese/pizza * 100)
