def solve(A, B):

    sum = 0
    for i in range(B):
        sum = sum + A[i]
    print(sum)
    max = float('-inf')
    j = len(A)-1
    for i in range(B-1,-1,-1):
        sum = (sum - A[i]) + A[j]
        if sum > max:
            max = sum
        print(i)
    
    return max


print(solve([5, -2, 3 , 1, 2],3))