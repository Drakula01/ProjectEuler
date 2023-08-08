def sqdiff(num):
    sqsum=0
    sumsq=0
    for n in range (0,num+1):
        sumsq += n**2
        sqsum += n
    sqsumf = sqsum**2
    return sqsumf - sumsq

num = int(input("Enter the limiting number:"))
print(sqdiff(num))


