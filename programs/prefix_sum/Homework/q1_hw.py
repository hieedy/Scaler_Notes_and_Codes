# Time to equality


# Method 1
class Solution:
    # @param A : list of integers
    # @return an integer

    def findMax(self,A):
        max_num = A[0]
        n = len(A)
        for i in range(1,n):
            if max_num < A[i]:
                max_num = A[i]
        return max_num

    def solve(self, A):
        max_num = self.findMax(A)
        
        sum_of_diff = 0
        n = len(A)
        for i in range(n):
            sum_of_diff += max_num - A[i]
        
        return sum_of_diff

# Method 2
class Solution:
    # @param A : list of integers
    # @return an integer

    def findMaxandSum(self,A):
        max_num = A[0]
        n = len(A)
        all_sum = A[0]
        for i in range(1,n):
            all_sum += A[i] 
            if max_num < A[i]:
                max_num = A[i]
        
        return max_num,all_sum

    def solve(self, A):
        max_num,all_sum = self.findMaxandSum(A)
        sum_of_diff = (max_num * len(A)) - all_sum
        
        return sum_of_diff