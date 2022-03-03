# Range SUm Query
#Important:
#Here I am taking PS array 1-based
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        n = len(A)
        output = []
        PS = [0]*(n+1)
        PS[0] = A[0]
        for i in range(1,n+1):
            PS[i] = PS[i-1]+A[i-1]

        for query in B:
            L = query[0]
            R = query[1]
           
            output.append(PS[R]-PS[L-1])
        
        
        
        return output

