num = input('Enter the number of digits: ')
num=int(num)
x = 0
max_pal = 0
for i in reversed(range(10**(num-1),10**num)):
    #print('**check i**')
    for j in reversed(range(10**(num-1),10**num)):
       # print('**check j**')
        prod=str(i*j)
        if prod == prod[::-1]:
            if i*j > max_pal:
                max_pal = i*j
print(max_pal)



