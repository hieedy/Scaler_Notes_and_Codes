# Count ways to make sum of odd and even indexed elements equal by removing an array element.
# Detail:  Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.


class Solution:
    # @param A : list of integers
    # @return an integer
       def solve(self, A):
        n = len(A)
        SE = [0] * n
        SO = [0] * n
        
        SE[0] = A[0]
        for i in range(1,n):
            
            if i&1 == 0:
                print(i)
                SE[i] =  SE[i-1]+A[i]
            else:
                SE[i] = SE[i-1]
        
        SO[0] = 0
        for i in range(1,n):
            
            if not i&1 == 0:
                SO[i] = SO[i-1]+A[i]
            else:
                SO[i] = SO[i-1]
        
        count = 0
        for i in range(n):

            if i == 0:
                sum_of_even = (SO[n-1] - SO[i])
                sum_of_odd = (SE[n-1]-SE[i])  
            else:
                sum_of_even = SE[i-1] + (SO[n-1] - SO[i])
                sum_of_odd = SO[i-1] + (SE[n-1]-SE[i])  


            if sum_of_even == sum_of_odd:
                count += 1

        return count



A=[2, 1, 6, 4]
sol = Solution()

print(sol.solve(A))

