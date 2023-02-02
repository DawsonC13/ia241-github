'''
lec3
list and set
'''

my_list = [ 1,2,3,4,5 ]
print(my_list)

print(type(my_list))

my_nested_list = [1,2,3,my_list]
print(my_nested_list)

my_list[0] = 6
print(my_list)

print(my_list[-1])

print(my_list[0:2])

print(my_list[:3])

my_list.append(7)
print(my_list)

my_list.remove(5)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list +[8,9] )

my_list.extend([8,9])
print(my_list)

print(len(my_list))

print('hello\tworld')

print('hello\nworld')

my_letters = ['a','a','b','b','c']
print(my_letters)
print(set(my_letters))

print('a' in my_letters)