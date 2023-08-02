#To find the sum of multiples of 3 & 5
#below a given number 
def sumof3n5(num):
    #num = input("Enter a number:")
    #num=int(num)
    sum=0
    for i in range(0,num):
        if i%3==0 or i%5==0:
            sum += i
    print(sum)

sumof3n5(10)
