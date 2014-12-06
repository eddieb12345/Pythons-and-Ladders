string = input('Please enter a string: ')

def vowel_count(STRING):

    #Total number of vowels
    total_count = int(STRING.count('a'))+int(STRING.count('e'))\
                  +int(STRING.count('i'))+int(STRING.count('o'))\
                  +int(STRING.count('u'))                                      

    #Prints the various vowels
    print('There are ' + str(STRING.count('a')) + ' as in the string.')        
    print('There are ' + str(STRING.count('e')) + ' es in the string.')
    print('There are ' + str(STRING.count('i')) + ' is in the string.')
    print('There are ' + str(STRING.count('o')) + ' os in the string.')
    print('There are ' + str(STRING.count('u')) + ' us in the string.')

    #Prints the total number of vowels
    print('The total number of vowels is ' + str(total_count) + '.')            

    return total_count

def rotate(STRING):                                                             
    new_string = ''                                                         

    for letter in STRING:                                                       
        #Checks if the letter is a-y
        if ord(letter) >= 97 and ord(letter) <= 121:                            
            #Increases each letter by one
            new_string = new_string + chr(ord(letter)+1)                        
        #Checks for z and makes it a
        elif letter == 'z':                                                  
            new_string = new_string + 'a'

    print('The rotation of the string is ' + new_string)

    return new_string
        
vowel_count(string)
rotate(string)
