def unit(t,n,k):
    if k >n:
        print("hi")
        return 0
    elif n % k !=0:
        return -1
    else:
        a = n//k 
        return a
        
if_name_=="__main__":
    
    t = int(input())
    n,k = input().split()
    n = int(n)
    k = int(k)