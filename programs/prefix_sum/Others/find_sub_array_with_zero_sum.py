# Find if there is a subarray with 0 sum

# We can also use hashing. The idea is to iterate through the array and for every element 
# arr[i], calculate the sum of elements from 0 to i (this can simply be done as sum += arr[i]). 
# If the current sum has been seen before, then there is a zero-sum array. 
# Hashing is used to store the sum values so that we can quickly store sum and 
# find out whether the current sum is seen before or not.
# ---------------------------------------------------------------------------------------------

##########Approach#####################
# If we consider all prefix sums, we can
# notice that there is a subarray with 0
# sum when :
# 1) Either a prefix sum repeats or
# 2) Or prefix sum becomes 0.

#var 1
def solve(A):
    """check if array contains subarray such that sum
    of elements of subarray is 0 """

    prefix_sum = set()
    is_exist = False
    sum = 0
    for i in range(len(A)):
        sum = sum+A[i]

        if sum in prefix_sum or sum == 0:
            return True
        
        prefix_sum.add(sum)
    

    print(prefix_sum)
    return is_exist


# A = [1, 4, -2, -2, 5, -4, 3]
# print(solve(A))

# ------------------------------------------------------------------------

# Vriations:
# count number of sub arrays such that sum is 0
# tell the index of subb-arrays (start and end) for those sum is 0.
# count number of sub array such that sum is K.

# Var-2

def solve(A):
    """check if array contains subarray such that sum
    of elements of subarray is 0 """

    prefix_sum = set()
    is_exist = False
    sum = 0
    for i in range(len(A)):
        sum = sum+A[i]

        if sum in prefix_sum or sum == 0:
            return True
        
        prefix_sum.add(sum)
    

    print(prefix_sum)
    return is_exist


A = [1, 4, -2, -2, 5, -4, 3]
print(solve(A))
