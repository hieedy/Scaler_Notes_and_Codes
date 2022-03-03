# def findPow(A,B):
#     if B == 0:
#         return 1
#     elif B == 1:
#         return A
#     elif B == 2:
#         return A*A
#     else:
#         split = B//2
#         return findPow(A,split) * findPow(A,B-split) 
    
    
    

# print(findPow(5,3))

def solve(A, B):
    
         
    hash_table = {}
    result = set()
    
    for  i in A:
        count=  hash_table.get(i)
        if count:
            hash_table[i] = hash_table[i] + 1
        else:
            hash_table[i] = 1
    
    for elem in B:
        
        count = hash_table.get(elem)
        
        if count and elem not in result:
            result.add(elem)
            
    
    return [elem for elem in result]


print(solve([2,4,1,2,3,4,7,8], [-1,2,6, ,8,10,11]))