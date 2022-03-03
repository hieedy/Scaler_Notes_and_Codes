
# Method 1:
# TC:- O(N^2)
# def subarraySum(A):

#     n = len(A)
#     total_sum = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum += A[j]
#             total_sum += sum
    
#     return total_sum
# A = [2, 1, 3]
# print(subarraySum(A))
            
def subArraysSum(A):
    n = len(A)
    sum = 0
    for i in range(n):
        sum += A[i] * (i+1)*(n-i)

    return sum


