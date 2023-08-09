# To find the largest prime number that is a factor of the given number
num = input("Enter the number:")
num=int(num)
div = num
factors=[]
while div>0:
    if num%div==0:
        #print(div)
        factors.append(div)
    div = div - 1
#print(factors)
primefactors = []
for i in factors:
    temp=[]
    for j in range (1,i+1):
        if i%j==0:
            temp.append(j)
        #print(temp)
    if len(temp)==2:
        primefactors.append(i)
print(max(primefactors))
