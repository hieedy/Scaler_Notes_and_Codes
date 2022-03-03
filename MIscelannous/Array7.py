from xml.etree.ElementTree import tostring


def Solve(A):
    n = len(A)
    candies = [1] * n

    for i in range(n-1):
        if A[i] > A[i+1] ad :
            candies[1] += 1
    
    for i in  range(n-1,0,-1):
        if A[i] > A[i-1]:
            candies[i] += 1
    
    return sum(candies)

A= [ -255, 369, 319, 77, 128, -202, -147, 282, -26, -489, -443, -401, 385, 465, -134 ]

print(Solve(A))

