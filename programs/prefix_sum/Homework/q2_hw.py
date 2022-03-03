class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        n = len(A)
        prod = [0]*n
        final_prod = 1
        
        for i in range(n):
            final_prod *= A[i]
        
        for i in range(n):
            prod[i] = final_prod//A[i]
        
        return prod

A = [5, 1, 10, 1]
sol = Solution()
print(sol.solve(A))


