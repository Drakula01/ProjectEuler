# Finding the maximum palindromic number obtained as a product of two n-digit numbers
num = input('Enter the number of digits: ')
num=int(num)
x = 0
max_pal = 0
for i in reversed(range(10**(num-1),10**num)):
    for j in reversed(range(10**(num-1),10**num)):
        prod=str(i*j)
        if prod == prod[::-1]:
            if i*j > max_pal:
                max_pal = i*j
print(max_pal)



