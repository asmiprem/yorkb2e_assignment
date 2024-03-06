

primeNumbers=[]
n=2
while n<100:
     isPrime=True
     for i in range (2,n):
     
          if n%i==0 and n!=i:
               isPrime=False
               break
     if isPrime:
          primeNumbers.append(n)
     n=n+1
print(primeNumbers)
     