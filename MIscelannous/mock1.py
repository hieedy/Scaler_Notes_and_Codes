def numSetBits(A):
    count = 0
    while A>0:
        if A&1 == 1:
            count = count+1
        
        A = A>>1
    
    return count

print(numSetBits(5))
        
def trailingZeros(A):
    count = 0
    while A>0:
        if A&1 == 0:
           count = count+1
        else:
            break
        A = A>>1

    return count

print(trailingZeros(8))     

