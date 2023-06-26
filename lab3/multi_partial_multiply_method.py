a = str(input("enter the multiplicand= "))
b = str(input("enter the multiplier= "))

print(f"Multiplicand = {a}, Multiplier = {b}")

j = -1
def addition(a,b):
    if (len(b) > len(a)):
        a = '0' * (len(b)-len(a)) + str(a)
    else: 
        b =  '0' * (len(a)-len(b))  + str(b)

    l = len(b)
    temp_sum = 0 
    j = -1
    carry = 0
    to_add  = ''

    result = ''
    for i in range(l):
        prev_carry = carry
        if ( b[j] == '0' ):
            carry = 0
            to_add = str(a[j])
        else:
            if( a[j] == '1'):
                carry = 1 
                to_add = '0'
            else: 
                carry = 0
                to_add = '1'
        j = j - 1

        temp_sum = int(to_add) + prev_carry
        if ( temp_sum == 2 ):
            to_add = '0' 
            carry = 1
        else:
            to_add = str(temp_sum)
        result =  to_add + result 

    return  str(carry) + result


print(addition(a,b))

partial_mul = ''
to_add = ''
result = ''
j = -1 
for i in range(len(b)):
    partial_mul =  ''
    for t in range(-1, -(len(a) +1 ), -1 ):
        to_add = str(int(a[t]) * int(b[j]))
        partial_mul = to_add + partial_mul
    partial_mul = partial_mul + '0' * i
    print(partial_mul)
    result =  addition(result, partial_mul)
    j = j-1 
print(f"Required result = {result}")
