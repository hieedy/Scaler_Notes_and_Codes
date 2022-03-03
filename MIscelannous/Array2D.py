
def hourglass(arr):

	output = []
	max = float('-inf')
	sum = 0
	for i in range(4):
		for j in range(4):
			sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]+arr[i+1][j+1]+ arr[i+2][j] +arr[i+2][j+1]+arr[i+2][j+2]
			if max < sum:
				max = sum
			sum = 0

	print(max)


TwoDArray = [
 [-9, -9, -9,  1, 1, 1],
 [0, -9,  0,  4, 3, 2],
 [-9, -9, -9,  1, 2, 3],
 [0,  0,  8, 6, 6, 0],
 [0,  0,  0, -2, 0, 0],
 [0,  0,  1,  2, 4,0],
 ]

hourglass(TwoDArray)

