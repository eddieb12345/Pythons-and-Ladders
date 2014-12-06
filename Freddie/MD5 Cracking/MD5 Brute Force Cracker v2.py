import hashlib

passhash = '1e685a8cce29c9bfbf747b9c5021e9c7'

found = False

guess_count = 0

charset1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
charset2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
charset3 = charset1 + charset2
charset4 = ['0','1']

charset_list = [charset1,charset2,charset3,charset4]

def guess(guess_string):
    global guess_count
    guess_count += 1
    #print(guess_string)
    for i in range(100):
        if guess_count == int(0.01*i*max_guesses):
            print(str(1*i) + '% of the maximum number of guesses done.')
    guess_hash = hashlib.md5(guess_string.encode('utf-8')).hexdigest()
    if guess_hash == passhash:
        print('The password is ' + guess_string)
        global found
        found = True

def crack_simpler(charsetnum,maxlength):                                                #A smarter version of the the algorithm
    charset = charset_list[charsetnum-1]                                                #The selected characters to try
    char_index = []                                                                     #A list of how many characters to try
    for l in range(maxlength):
        char_index.append(l+1)                                                          #Adds a character for each character in the maximum length
    print(char_index)
    global max_guesses
    max_guesses = len(charset)**maxlength                                               #Calculates how many guesses it could take
    print('The maximum number of guesses it will take is ' + str(max_guesses))
    for i in range(maxlength):
        l = i+1
        for char1 in charset:
            if l == 1:
                if found == False:
                    guess_string = char1
                    guess(guess_string)
            elif l == 2:
                for char2 in charset:
                    if found == False:
                        guess_string = char2+char1
                        guess(guess_string)
            elif l == 3:
                for char2 in charset:
                    for char3 in charset:
                        if found == False:
                            guess_string = char3+char2+char1
                            guess(guess_string)         
            elif l == 4:
                for char2 in charset:
                    for char3 in charset:
                        for char4 in charset:
                            if found == False:
                                guess_string = char4+char3+char2+char1
                                guess(guess_string)
            elif l == 5:
                for char2 in charset:
                    for char3 in charset:
                        for char4 in charset:
                            for char5 in charset:
                                if found == False:
                                    guess_string = char5+char4+char3+char2+char1
                                    guess(guess_string) 
    if found == False:
        print('Password not found.')

def crack_basic(charsetnum,maxlength):
    charset = charset_list[charsetnum-1]
    global max_guesses
    max_guesses = len(charset)**maxlength
    print('The maximum number of guesses it will take is ' + str(max_guesses))
    for i in range(maxlength):
        l = i+1
        for char1 in charset:
                if l == 1:
                    guess_string = char1
                    guess(guess_string)
                    if found == True:
                        break
                elif l == 2:
                    for char2 in charset:
                        guess_string = char2+char1
                        guess(guess_string)
                        if found == True:
                            break
                    if found == True:
                        break
                elif l == 3:
                    for char2 in charset:
                        for char3 in charset:
                            guess_string = char3+char2+char1
                            guess(guess_string)
                            if found == True:
                                break
                        if found == True:
                            break
                    if found == True:
                        break            
                elif l == 4:
                    for char2 in charset:
                        for char3 in charset:
                            for char4 in charset:
                                guess_string = char4+char3+char2+char1
                                guess(guess_string)
                                if found == True:
                                        break
                            if found == True:
                                break
                        if found == True:
                            break
                    if found == True:
                        break
                elif l == 5:
                    for char2 in charset:
                        for char3 in charset:
                            for char4 in charset:
                                for char5 in charset:
                                    guess_string = char5+char4+char3+char2+char1
                                    guess(guess_string)
                                    if found == True:
                                        break
                                if found == True:
                                    break
                            if found == True:
                                break
                        if found == True:
                            break
                    if found == True:
                        break  
    
    if found == False:
        print('Password not found.')

def crack_help():
    print('Character set 1 is all lowercase letters.')
    print('Character set 2 is all uppercase letters.')
    print('Character set 3 is all letters.')
    #print('Character set 1 is all lowercase letters.')

def c(charsetnum,maxlength):                    #Shortcut to crack_simpler
    crack_simpler(charsetnum,maxlength)

    
charsetnum,maxlength = eval(input('Please enter the character set you want to use and the maximum length you wish to crack to. Type crack_help() for more information. '))

crack_simpler(charsetnum,maxlength)



                            
