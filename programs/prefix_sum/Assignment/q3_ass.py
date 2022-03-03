# Pick from both sides!
# Add from left side 0 to < B
# start from left side >=n-B and keep on subtracting and checking the max_sum

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_sum = 0
        curr_sum = 0
        n = len(A)
        for i in range(0,B):
            max_sum += A[i]


          
        curr_sum = max_sum
        j = n-1
        temp = B-1
        while j>=n-B:
            curr_sum -= A[temp]
            curr_sum += A[j]
            
            if  curr_sum > max_sum:
                max_sum = curr_sum
            
            temp -=1
            j -= 1

        print(max_sum)

A = [1, 2]
sol = Solution()
sol.solve(A,1)
    

# TC = O(N)

