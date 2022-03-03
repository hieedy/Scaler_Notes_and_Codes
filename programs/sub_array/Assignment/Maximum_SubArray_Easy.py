# Q4. Maximum Subarray Easy
# They have removed the restriction of TLE here/

# TC - O(N^2)
def maxSubarray(A, B, C):
    
    curr_sum = float('-inf')
    for i in range(A):
        sum = 0
        for j in range(i,A):
            sum += C[j]

            if sum > curr_sum and sum <= B:
                curr_sum = sum
    return curr_sum if curr_sum != float('-inf') else 0

A = 5
B = 12
C = [2, 1, 3, 4, 5]
print(maxSubarray(A,B,C))



