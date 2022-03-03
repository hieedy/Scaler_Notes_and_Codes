def solve(A):
	left_max = [0 for i in A]
	right_min = [0 for i in A]
	n = len(A)
	left_max[0] = A[0]
	for elem in range(1,n):
		if A[elem] > left_max[elem-1]:
			left_max[elem] = A[elem]
		else:
			left_max[elem] = left_max[elem-1]

	print(left_max)
	right_min[-1] = A[-1]
	for elem in range(n-2,-1,-1):
		if A[elem] < right_min[elem+1]:
			right_min[elem]  = A[elem]
		else:
			right_min[elem]  = right_min[elem+1]

	print(right_min)

	flag = False
	for i in range(1,n):
		if A[i] > left_max[i-1] and A[i]<right_min[i+1]:
			flag = True
			break

	return flag

		

print(solve([ 5706, 26963, 24465, 29359, 16828, 26501, 28146, 18468, 9962, 2996, 492, 11479, 23282, 19170, 15725, 6335 ]
))