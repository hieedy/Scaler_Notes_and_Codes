class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        flag = 0
        #sort the array
        A.sort()
        #keep the pointer at the end of the array
        i = n - 1
        # keep going backwards until we dont find a different element
        while(flag == 0 and i != 0):
            if(A[i] == A[i-1]):
                i -= 1
            else:
                flag = 1
        #if we find a different element before reaching the end of the array, print the element at the index before that
        #else return 0 because in that case all the elements are same and no matter which indices we choose, the answer will always be 0
        if(i != 0):
            return A[i-1]
        else:
            return 0

            