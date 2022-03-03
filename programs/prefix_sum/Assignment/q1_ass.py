# Equilibrium index of an array

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        PS = [0]*n
        PS[0] = A[0]
        for i in range(1,n):
            PS[i] = PS[i-1] + A[i]
        
        for i in range(n):
            if i!=0:
                Sl = PS[i-1]
            else:
                Sl = 0
                
            Sr = PS[n-1] - PS[i]

            if Sl == Sr:
                return i
        
        return -1
