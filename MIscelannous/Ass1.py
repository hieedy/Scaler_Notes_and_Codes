
def solve(A):
    
    max_even  = float('-inf')
    min_odd = float('inf')
    
    for value in A:
        if value%2==0:
            ## it means this is even 
            if max_even < value:
                max_even = value
        else:
            ## it means it is odd
            if min_odd > value:
                min_odd  = value
    
    print(min_odd, max_even)
    return max_even - min_odd



print(solve([1,2,4,5,7,9,10,20,133,120]))