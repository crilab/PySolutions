import math

width = 27
line = '-' * width

print('Hot Dog Planner'.center(width))
print(line)
print()
print('How many students want:')
print()
hotdogs_two = int(input('Two ordinary hotdogs? '))
print()
hotdogs_three = int(input('Three ordinary hotdogs? '))
print()
vegan_two = int(input('Two vegan hotdogs? '))
print()
vegan_three = int(input('Three vegan hotdogs? '))
print()

hotdog_total = hotdogs_two * 2 + hotdogs_three * 3
vegan_total = vegan_two * 2 + vegan_three * 3
drink_total = hotdogs_two + vegan_two + hotdogs_three + vegan_three

hotdog_packages = math.ceil(hotdog_total / 8)
vegan_packages = math.ceil(vegan_total / 4)

hotdog_cost = hotdog_packages * 20.95
vegan_cost = vegan_packages * 34.95
drink_cost = drink_total * 13.95
total_cost = hotdog_cost + vegan_cost + drink_cost

hotdog_cost = round(hotdog_cost, 2)
vegan_cost = round(vegan_cost, 2)
drink_cost = round(drink_cost, 2)
total_cost = round(total_cost, 2)

print(line)
print('AMOUNT  ITEM           COST')
print()
print(str(hotdog_packages).ljust(8) + 'HOT DOGS' + str(hotdog_cost).rjust(11))
print(str(vegan_packages).ljust(8) + 'VEGAN' + str(vegan_cost).rjust(14))
print(str(drink_total).ljust(8) + 'DRINKS' + str(drink_cost).rjust(13))
print()
print(line)
print()
print(f'TOTAL: {total_cost}:-')
