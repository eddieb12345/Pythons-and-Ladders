string1 = input('Please input a string: ')

def reverse_string(string1):
    string2 = ''
    for n in range(len(string1)-1,-1,-1):
        string2=string2 + string1[n]
    print(string2)    
reverse_string(string1)

    



             
