n=1
prime_list=[]
for i in range (1,10000):
    while n<100000:
        n=n+1
        if n%i==0 and n !=i:
            continue
        prime_list=i+prime_list
        print(prime_list)



        

    
