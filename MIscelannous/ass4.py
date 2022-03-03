# def solve(A):
#     if A==1:
#        return 1
#     output = 1
#     for i in range(2,A): #[Here I can add range (1,A+1) also that doesnot matter as our loop will be executing till A//i only]
#         if i <= A//i:
#             if A%i==0:
#                 output = i
#         else:
#             break                

#     print(output)
#     if i*i == A:
#         return i
#     else:
#         return -1


# print(solve(36))


# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output

#     num = int(input())
#     equals_to = num

#     for i in range(1,11):
#         print(f"{num} * {i} = {equals_to}")
#         equals_to = equals_to+num

#     return 0

# if __name__ == '__main__':
#     main()



def isArmstrong(num):

    sum_of_cube_of_digits = 0
    temp = num
    while num>0:
        rem = num%10
        sum_of_cube_of_digits = sum_of_cube_of_digits + (rem*rem*rem)
        num = num//10

    

    if sum_of_cube_of_digits == temp:
        return True
    else:
        return False




def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    num = int(input())

    for i in range(0,num+1):
        if isArmstrong(i):
            print(i)


if __name__ == '__main__':
    main()


