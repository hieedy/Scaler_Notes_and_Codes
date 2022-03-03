import math
from turtle import right
# class Solution:
#     def solve(self, A):
#         min_elem = max_elem = A[0]
#         n = len(A)
#         for i in range(1,n):
#             if min_elem > A[i]:
#                 min_elem = A[i]
            
#             if max_elem < A[i]:
#                 max_elem = A[i]
        
#         print(min_elem, max_elem)

#         left_min = []
#         right_min = [0]*n
        
#         #[1,2,0,4,5,8,2,0,8,0,0,4,2,8]
#         left_min.append(-1 if A[0] != min_elem else 0)
#         for i in range(1,n):
#             if A[i] == min_elem:
#                 left_min.append(i)
#             else:
#                 left_min.append(left_min[i-1])

#         right_min[-1] = -1 if A[-1] != min_elem else n-1
#         for i in range(n-2,-1,-1):
#             if A[i] == min_elem:
#                 right_min[i] = i
#             else:
#                 right_min[i] = right_min[i+1]
       
#         min_length = n+1
#         for i in range(n):
#             if A[i] == max_elem:
#                 left_min_position = left_min[i]
#                 right_min_position = right_min[i]

#                 left_length = n+2
#                 right_length = n+2
#                 if left_min_position != -1:
#                     left_length = abs(i- left_min_position) + 1

#                 if right_min_position != -1:
#                     right_length = abs(i - right_min_position) + 1

#                 min_length = min(right_length, left_length, min_length)

#         return min_length        

# ----------------------------------------------------

#Method 2 without using Space

class Solution:
    def solve(self, A):
        min_num = max_num = A[0]
        n = len(A)
        for i in range(n):
            if A[i]<min_num:
                min_num = A[i]
            elif A[i]>max_num:
                max_num = A[i]

        left_ind = -1
        ans = n+1
        for i in range(n):
            if A[i] == max_num:
                left_ind = i
            
            if A[i] == min_num and left_ind != -1:
                temp = i-left_ind+1
                ans = min(ans, temp)
        
        right_ind = -1
        for i in range(n-1,-1,-1):
            if A[i] == max_num:
                right_ind = i
            
            if A[i] == min_num and right_ind != -1:
                temp = right_ind - i + 1
                ans = min(ans, temp)
        
        return ans












        
A = [1,2,0,4,5,8,2,0,8,0,0,4,2,8]
sol = Solution()
print(sol.solve(A))

