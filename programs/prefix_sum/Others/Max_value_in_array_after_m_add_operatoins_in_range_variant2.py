def solve(A,queries):
    # A is not zeros array
    n = len(A)
    temp = [0]*n
    for query in queries:
        a = query[0]-1
        b = query[1]-1
        k = query[2]

        temp[a] = temp[a]+k
        
        if b == len(A)-1:
            continue
        
        temp[b+1] = temp[b+1] - k
    
       

    #find prefix_sum of that temp

    for i in range(1,n):
        temp[i] = temp[i-1] + temp[i]
    
    max_num = A[0]
    for i in range(0,n):
        A[i] = A[i] + temp[i]

        if max_num < A[i]:
            max_num = A[i]

    print(f"final array after m operation : - {A}")
    return max_num


A = [1,2,3,4,5]
B = [
    [2,4,5],
    [1,3,5],
    [1,2,5],
    [3,5,5]
]

print(f"Maximum in the new array after m operation {solve(A,B)}")

