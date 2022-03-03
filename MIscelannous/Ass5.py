# def solve(A):
# 	max_sum = float('-inf')
# 	n = len(A)
# 	for i in range(n):
# 		temp = A[i]
# 		for j in range(i+1,n):

# 			if temp > max_sum:
# 				max_sum = temp

# 			temp = temp+A[j]

# 	return max_sum

# print(solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maxSubArraySum(a,size):
      
    max_so_far = float('-inf')
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far
  
# Driver function to check the above function
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))