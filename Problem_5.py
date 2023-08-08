# To find the smallest multiple of first n numbers
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def smallest_multiple(num):
    temp = list(range(1,num+1))
    lcm = 1
    for i in range(num):
        lcm = (lcm*temp[i])/gcd(lcm,temp[i])
    return lcm
if __name__ == "__main__":
    n = int(input ("Enter the limiting number:"))
    print(int(smallest_multiple(n)))


