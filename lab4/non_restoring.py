from addition import addition
from subtraction import subtraction

dividend = str(input("Dividend = "))
divisor  = str(input("Divisor = "))

A = ''
A = A.zfill(5)
M = divisor.zfill(5)
# print('Divisor = ', M)
Q = dividend.zfill(4)
n = 4 
temp  = ''


    
for i in range(1,5):
    temp =  A + Q
    
    if ( A[0] == '0'):
        temp = temp[1:]
        A = temp[:5]
        Q = temp[-3:]
        A = subtraction(A, M)
    else:
        temp = temp[1:]
        A = temp[:5]
        Q = temp[-3:]
        A = subtraction(A, M)

    if (A[0] == '1' ):
        Q = Q + '0' 
        print( Q)
        A = addition(A, M)
        print(A)
    else:
        Q = Q + '1'
        print(A)
    print("----------------------------------")


if (A[0] == '1' ):
    A = addition(A, M)

print("Remainder = ", A)
print("Quotient = ", Q)






