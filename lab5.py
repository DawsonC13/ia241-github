#3.1
alien_color = 'red'
if alien_color == 'green':
    print('you got 5 points')
    
#3.2
alien_color = 'red'
if alien_color == 'green':
    print('you got 5 points')
else:
    print('you got 10 points')
    
#3.3
favorite_fruits = ('bananas', 'apples', 'oranges')
if 'apples' in favorite_fruits:
    print('I love apples')
if 'oranges' in favorite_fruits:
    print('I love oranges')
if 'bananas'in favorite_fruits:
    print('I love bananas')

#3.4
age = 73
if age <=10:
    print('kid')
elif 20>age>=10:
    print('teenager')
else :
    print('adult')
    if age>=65:
        print('elder')