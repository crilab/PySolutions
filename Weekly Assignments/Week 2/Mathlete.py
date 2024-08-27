line = '-------------------'

print('.: MATHLETE v2.0 :.')
print(line)

total_sum = 0
cardinality = 0

while True:
    i = input('> ')
    try:
        total_sum += float(i)
        cardinality += 1
    except ValueError:
        if i == 'exit':
            break
        print('ERROR: Invalid number')

try:
    mean_value = total_sum / cardinality
except ZeroDivisionError:
    mean_value = 'undefined'

print(line)
print('Cardinality:', cardinality)
print('Sum:        ', total_sum)
print('Mean value: ', mean_value)
