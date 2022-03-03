# An Example Problem : 
# Consider an array of size n with all initial values as 0. Perform the given ‘m’ add operations from index ‘a’ to ‘b’ and evaluate the highest element in the array. An add operation adds 100 to all elements from a to b (both inclusive). 
#Problem link :- https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/ 



# for all m queries do add from a to b everytime in an array
# and at last find max and return that max element.
# TC = O(N*q)

#Optimized
def solve(A,queries):
    #A will alway be initialized to zero
    for query in queries:
        a = query[0]-1
        b = query[1]-1

        A[a] = A[a]+100

        if b == len(A)-1:
            continue

        A[b+1] = A[b+1] - 100
    
    # find prefix of A
    prefix_sum = [0]*len(A)
    prefix_sum[0] = A[0]
    max_num = A[0]
   
    for i in range(1,len(A)):
        prefix_sum[i] = prefix_sum[i-1] + A[i]

        if max_num < prefix_sum[i]:
            max_num = prefix_sum[i]
    
    return max_num



A = [0,0,0,0,0]
B = [
    [2,4],
    [1,3],
    [1,2],
    [3,5]
]

print(solve(A,B))