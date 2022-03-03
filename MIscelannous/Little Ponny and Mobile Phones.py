#Little pony is going to buy some mobile phones for his friends. As there many models available in the market at #different prices, He is confused and wants to know the maximum distinct models of a mobile phone he can buy for his 3friends, given that he has a total X amount of money.
#You are given an array A of size N. denoting the size of prices of different models. The array is sorted based on #prices in increasing order. You are given another array B of size Q denoting the queries. In i'th query, you need to #tell the maximum distinct models of mobile phones he can buy with B[i] money.

# Brute-Force
# def solve(A,B):

# 	result = [0 for i in B]
# 	n = len(A)
# 	m = len(B)
# 	for i in range(m):

# 		add = 0

# 		count = 0

# 		for item in A:
# 			add = add + item
# 			if add<= B[i]:
# 				count = count+1
# 			else:
# 				break

# 		result[i] = count

# 	return result


# output = solve([2,3,5],[5])
# print(output)

def findUpperBound(money, prefix_sum):
	#using BInary Search as the list is sorted

	upper_bound = -1
	start = 0
	end = len(prefix_sum) -1

	while start<=end:

		mid = start+(end-start)//2

		if prefix_sum[mid] == money:
			return mid+1
		elif prefix_sum[mid] > money:
			end = mid-1
		else:
			start = mid + 1


	return end+1





def solve(A,B):
	result = [0 for i in B]
	prefix_sum = [0 for i in A]

	prefix_sum[0]  = A[0]
	n = len(A)
	m = len(B)
	for i in range(1,n):
		prefix_sum[i] = prefix_sum[i-1]+A[i]

	print(prefix_sum)

	for i in range(m):

		upper_bound = findUpperBound(B[i],prefix_sum)
		print(upper_bound)
		result[i] = upper_bound

	return result

print(solve([ 23, 36, 58, 59 ],[ 3, 207, 62, 654, 939, 680, 760 ]))
