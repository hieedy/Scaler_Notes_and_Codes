
def findTranspose(arr):
	for i in range(len(arr)):
		for j in range(i,len(arr[i])):
			temp = arr[i][j]
			arr[i][j] = arr[j][i]
			arr[j][i] = temp

	return arr

def reverseColumns(arr):

	for i in range(len(arr)):
		n = len(arr[i])-1
		for j in range(n//2+1):
			temp = arr[i][j]
			arr[i][j] = arr[i][n-j]
			arr[i][n-j] = temp
	return arr

def rotateArray90Deg(arr):
	arr = findTranspose(arr)
	printArray(arr)
	arr = reverseColumns(arr)
	printArray(arr)


	return arr

def printArray(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			print(arr[i][j], end= " ")
		print()


arr = [
    [3, 1],
    [4, 2]
]

print(rotateArray90Deg(arr))