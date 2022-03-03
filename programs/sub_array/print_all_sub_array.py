def printSubArray(A, i,j):
    for i in range(i,j+1):
        print(A[i], end = " ")

def printAllSubArray(A):
    n = len(A)

    for i in range(n):
        for j in range(i,n):
            # for k in range(i,j+1):
            #     print(A[k], end=" ")
            printSubArray(A,i,j)
            print()
        print("---------------------------")


A = [1,2,3,4,5,6,7]
printAllSubArray(A)