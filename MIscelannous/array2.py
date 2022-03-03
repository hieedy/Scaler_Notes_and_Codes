def solve(A):

        n = len(A)
        count_even = 0
        count_odd = 0
        for i in range(n):
            is_even = A[i]%2 == 0

            if is_even:
                count_even  = count_even + 1
            else:
                count_odd = count_odd + 1
                
        
        print(count_even, count_odd)

solve([ 33, 82, 75, 4, 52, 74, 79, 46, 18, 73, 1, 83, 46, 94, 44, 86, 40, 1, 46, 24, 99, 16, 88, 6, 66, 17, 1 ])