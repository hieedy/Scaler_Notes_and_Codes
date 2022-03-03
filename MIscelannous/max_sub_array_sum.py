def incrementor(i):
	return i+1

def solve(A):
	max_sum = [0 for i in A]
	sum = 0
	j = 0
	for i in A:
		sum = sum+i
		max_sum[j] = sum 
		j = incrementor(j) 

	print(max_sum)
	max_result = float('-inf')
	for i in max_sum:
		if i > max_result:
			max_result = i


	return max_result


print(solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
