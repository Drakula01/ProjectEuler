def evenfibonacci(num):
    sum=0
    fibo = [1,2]
    for i in range(0,num-2):
        fibo.append(fibo[i]+fibo[i+1])
    #print(fibo)
    for j in fibo:
        #print(j)
        if j%2 == 0 and j<=num:
            sum += j
    print(sum)

evenfibonacci(60)

