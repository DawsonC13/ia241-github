'''
lec7
while loop
continue, break, and pass
'''
'''
for item in ['a', 'b']:
    print(item)
    i=5
    while i > 0:
        i = i - 1
    
        if i ==3:
            continue
        print(i)
'''        

i=5
while i >=0:
    i = i - 1
    
    if i ==3:
        pass
    
    print(i)
try:
    print(1/0)
except :
    print('error')