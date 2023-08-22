def nthprime(n):
    primes = [2]
    i=3
    while len(primes) < n:
        for num in primes:
            if i % num == 0:
                break
            elif i % num != 0:
                if num == primes[len(primes)-1]:
                    primes.append(i)
                else:
                    continue
        i += 2
    return primes[n-1]

if  __name__ == "__main__":
    n = int(input("Enter the limiting number: "))
    print(nthprime(n))



