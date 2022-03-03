# print all the subarrays
def printAllSubArrays(A):
    n = len(A)
    for i in range(n):
        print("All subarrays starting from index",i)
        for j in range(i,n):
            for k in range(i,j+1):
                print(A[k],end=" ")
            print()
        print("------------------------------------")
##################################################################################

# print sum of all the individual subarrays
def sum_of_subarray(A,i,j):
    sum = 0
    for idx in range(i,j+1):
        sum += A[idx]
    
    return sum

def getSumOFSubArray(A):
    n = len(A)
    for i in range(n):
        for j in range(i,n):
            print(sum_of_subarray(A,i,j)) # u can do the same using another for loop
        print("-------------------")


def efficient_getSumOfSubArray(A):
    n = len(A)
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += A[j]
            print(sum)
        print("--------------------")


####################################################################

# How many subArrays are there for a given index:
# let's say you are giben index 0 how many sub-arrays will be there
# starting from ibdex 0 ?
# Ans = n

# if i say index 2 ?
# then subarrays starting from index 2 will be n-2
# So I can say sub-arrays starts from given index will be (n-i)
def count_subArraysStartingFromGivenIndex(A,idx):
    n = len(A)        
    if idx < n:
        return (n-idx)
    else:
        print('Index cannot be greated then ',n)

##########################################################################

# for a given index i how many subarrays will be there which are 
# ending at index i

# example A = [5,7,8,1,2]
# i = 3
# How many subarrays will be there ending at index 3 i.e. ending  with value 1
# in our example it would be
# [5,7,8,1]
# [7,8,1]
# [8,1]
# [1]
# so in genral i can say it will be (i+1)

# example for index 1 how many subarrays will end with index 1 ?
# 1+1 == > 2 i.e. only 2 subarrays are possible which are ending with idx 1

def count_subArraysEndingWithGivenIndex(A,idx):
    return idx+1

#####################################################################################

# for a given index i for how many subbarays that index will be a part of.
# example idx = 2
# tell me the number of sub_arrays which will contain idx = 2 anywhere in the list 
# num_of_sub_array_ending_with_idx * num_of_sub_array_starting_with_idx
# (i+1) * (n-1 - i + 1) ===> (i+1)* (n-i)

def count_subArraysContainsGivenIndex(A,idx):
    n = len(A)
    return (idx+1)*(n-i)



A = [1,2,3,4,5]
# printAllSubArrays(A)
# getSumOFSubArray(A)

# efficient_getSumOfSubArray(A)
# print(count_subArraysStartingFromGivenIndex(A,0))
print(count_subArraysEndingWithGivenIndex(A,2))