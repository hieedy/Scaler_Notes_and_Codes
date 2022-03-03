def solve(A):
	n = len(A)
	output = -1
	for i in range(1,n-1):
		flag = True
		#left
		for j in range(i-1,-1,-1):
			if not A[j]<A[i]:
				flag = False
				break
		if not flag:
			continue
		#right
		for j in range(i+1,n):
			print(A[j])
			print(j)
			if not A[j]>A[i]:
				flag = False
				break
		if flag:
			output = A[i]
			break
	return (flag,output)

print(solve([ 5706, 26963, 24465, 29359, 16828, 26501, 28146, 18468, 9962, 2996, 492, 11479, 23282, 19170, 15725, 6335 ]
))