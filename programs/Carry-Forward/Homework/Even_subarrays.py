class Solution:
    # @param A : list of integers
    # @return a strings

    def isEven(self,num):
        return num%2==0

    def solve(self, A):
        ans = 'NO'  
        n = len(A)

        if n%2 == 1:
            return ans
        else:
            for i in range(1,n-1):
                if (
                    self.isEven(A[i]) and
                    self.isEven(A[0]) and 
                    self.isEven(A[n-1]) and 
                    self.isEven(A[i+1])
                ):
                    ans = 'YES'
                    return ans 

        return ans

A = [ 654, 50, 694, 750, 712, 275, 736, 146, 279, 816, 707, 396, 406, 589, 370, 742, 840, 290, 505, 23, 249, 447, 618, 80, 968, 189, 600, 662, 91, 604, 575, 689, 72, 196, 475, 198, 850, 844, 361, 419, 617, 911, 268, 628, 408, 404, 477, 921, 478, 806, 204, 637, 403, 911, 589, 529, 867, 584, 768, 257, 437, 380, 698, 452, 368, 97, 977, 582, 775, 103 ]

sol = Solution()
print(sol.solve(A))
