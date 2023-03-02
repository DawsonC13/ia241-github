'''
lab 7
'''

#3.1
i = -1
while i < 5:
    i = i + 1
    if i ==3:
        continue
    print(i)
    
#3.2
i = 1
result = 1
while i <= 5:
    result = result * i
    i = i + 1
print(result)

#3.3
i = 1
result = 0
while i <= 5:
    result = result + i
    i = i + 1
print(result)

#3.4
i = 3
result = 1
while i <= 8:
    result = result * i
    i = i + 1
print(result)

#3.5
i = 8
result1 = 1
while i >= 1:
    result1 = result1 * i
    i = i - 1 

n = 3
result2 = 1
while n >= 1:
    result2 = result2 * n
    n = n - 1

print(result1/result2)

#3.6
num_list = [12, 32, 43, 35]
while num_list:
    num_list.pop()
    print(num_list)

