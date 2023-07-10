def addition(a,b):
    a = a.zfill(5)
    b = b.zfill(5)

    # print(f"a ={a}, b = {b}")

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

    if (str(carry) == 1 ):
        return  str(carry) + result
    else:
        return result

