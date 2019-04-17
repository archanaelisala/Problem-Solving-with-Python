def computeGCD(a, b):

# choose the smaller number
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
            
    return gcd

n1 = int(input("Enter a first value:"))
n2 = int(input("Enter a second value:"))


print("The gcd of", n1,"and", n2,"is", computeGCD(n1, n2))
