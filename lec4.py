'''
lec4
dict and tuple
'''

my_tuple = ('a', 'b', 'c', 'd', 'e')

#my_tuple[0]='f' cannot reassign tuple values, tuple has a comma, if no commma it's a string
print(my_tuple)

'''
dictionary can be used with {} and dict()
{k:v, k:v, k:v}
'''

my_car = { 'color':'red', 'make':'toyota', 'year':'2015' }
#print(my_car.items())
#print(my_car.keys())
#print(my_car.values())
#print(my_car.get('color')) same as print(my_car['color'])
my_car['model'] = 'venza'
print(my_car)
#my_car['year'] = 2020
#print(my_car)
print(len(my_car))

print('red' in my_car.values())