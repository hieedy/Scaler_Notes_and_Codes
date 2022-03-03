# Method 1
# TC = O(N^2) in worst case
# def solve(A,B):
#     n = len(A)
#     least_average = float('inf')
#     least_average_idx = -1
#     for i in range(n-B+1):
#         sum = 0
#         for j in range(i,B+i):
#             sum += A[j]
#         avg = sum/B
#         if avg < least_average:
#             least_average = avg
#             least_average_idx = i
#         print(f"from index {i} to {j} average is {avg}")
    
#     return least_average_idx

################################################################
#Method 2
def solve(A,B):
    sum = 0
    n = len(A)
    for i in range(B):
        sum += A[i]
    
    least_sum_avg = sum/B
    least_sum_avg_idx = 0

    i = 1
    j = B

    while j < n:
        sum -= A[i-1]
        sum += A[j]

        avg = sum/B

        if avg < least_sum_avg:
            least_sum_avg = avg
            least_sum_avg_idx = i
        
        print(f"Avg from index {i} to {j} is {avg}")
        i += 1
        j += 1

    return least_sum_avg_idx











A = [ 1,2,3,4,5 ]
B = 2
print(A[solve(A,B)])

