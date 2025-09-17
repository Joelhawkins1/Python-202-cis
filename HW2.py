import math
p1 = int(input("How many slices will person 1 eat? "))
p2 = int(input("How many slices will person 2 eat? "))
p3 = int(input("How many slices will person 3 eat? "))
p4 = int(input("How many slices will person 4 eat? "))

total = p1 + p2 + p3 + p4

slices = 8

order = math.ceil(total / slices)
pizzaleft = (order*slices) % total

print(f'You need {order:.0f} pizzas and will have {pizzaleft:.0f} slices left')
