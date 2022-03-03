from os import stat


def isAlernateArray(A,i,j):
    state = A[i]
    result = True
    for idx in range(i,j+1):
        if A[idx] == state:
            if state == 0:
                state = 1
            else:
                state = 0
        else:
            result = False
            break
        
    return result
        



def solve(A,B):
    if B == 0:
        return list(range(len(A)))
    else:
        output = []
        n = len(A)
        end = n-B-1
        for i in range(B,end+1):# because I want to consider that end idx itself.
            print(i-B,i+B)
            if isAlernateArray(A,i-B,i+B):
                output.append(i)
        
        return output


A  = [1, 0, 1, 0, 1]
print(solve(A,1))

