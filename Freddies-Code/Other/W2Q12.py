n = input('Please input an integer: ')

def reverse_integer(n):
    stringOfInt1 = str(n)
    stringOfInt2 = ''
    for n in range(len(stringOfInt1)-1,-1,-1):
        stringOfInt2=stringOfInt2 + stringOfInt1[n]
    return(int(stringOfInt2))    

print('The integer reversed is' , reverse_integer(n))

    



             
