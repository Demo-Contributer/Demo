def fibo(n):
    l = [0] * (n+1)
    l[1]= 1
    
    for i in range (2,n+1):
        l[i] = l[i-1] + l[i-2]
    return l
    
 
print(fibo(50))
