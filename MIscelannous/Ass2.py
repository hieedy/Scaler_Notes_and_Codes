def solve(A, B):
        
        size = len(A)
        count_pairs = 0    
        for i in range(size):
            for j in range(i+1, size):
                if A[i]+A[j] == B:
                    count_pairs += 1
    
        
        return count_pairs       


print(solve([1,1,1], 2))