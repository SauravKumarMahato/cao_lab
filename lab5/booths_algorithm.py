from two_s_comp  import two_s_comp 
from two_s_comp import addition
from two_s_comp import subtraction

multiplicand = str(input("Multiplicand = "))
multiplier  = str(input("Multiplier = "))

multiplicand = multiplicand.zfill(4)
multiplier = multiplier.zfill(4)


A = '0000'
B = multiplicand
Q = multiplier
Q_minus_one = '0'
temp = ''

def arith_shift_right( A, Q, Q_minus_one, temp):
    temp = A + Q + Q_minus_one
    temp = temp[:-1]
    temp = temp[0] + temp
    A = temp[:4]
    Q = temp[4:8]
    Q_minus_one = temp[-1]

    return A,Q,Q_minus_one, temp


for i in range(1,5):
    if Q[-1] == '0' and Q_minus_one == '1'  :
        # ASR operation
        A = addition(A, B)
        A,Q,Q_minus_one , temp= arith_shift_right(A,Q,Q_minus_one,temp)
        

    elif Q[-1] == '1' and Q_minus_one == '0'  :
        A = subtraction(A,B)
        A,Q,Q_minus_one, temp = arith_shift_right(A,Q,Q_minus_one, temp)
        
    else:
        A,Q,Q_minus_one, temp = arith_shift_right(A,Q,Q_minus_one, temp)


print("The required answer is : ", temp[:-1])


    



