import hashlib

passhash = '1e685a8cce29c9bfbf747b9c5021e9c7'

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
        if guess_count == int(0.1*i*max_guesses):
            print(str(10*i) + '% of the maximum number of guesses done.')
    guess_hash = hashlib.md5(guess_string.encode('utf-8')).hexdigest()
    if guess_hash == passhash:
        print('The password is ' + guess_string)
        global found
        found = True

def crack_recurse(charset,maxlength):
    global guess_string
    global current_length
    if found == False:
        current_length += 1
        for char in charset:
            print('The length is ' + str(current_length) +'. The character guess is ' + char + '. The guess before adding is ' + guess_string)
            guess_string = guess_string + char
            print('The new guess is ' + guess_string)
            if current_length < maxlength:
                crack_recurse(charset,maxlength)
            else:
                guess(guess_string)

def crack_v4(charsetnum,maxlength):                                                     #An iterative version of the the algorithm
    global found
    found = False
    global guess_count
    guess_count = 0
    global guess_string
    guess_string = ''
    charset = charset_list[charsetnum-1]                                                #The selected characters to try
    global max_guesses
    max_guesses = len(charset)**maxlength                                               #Calculates how many guesses it could take
    print('The maximum number of guesses it will take is ' + str(max_guesses))
    global current_length
    current_length = 0
    crack_recurse(charset,maxlength)
    if found == False:
        print('Password not found.')



def crack_v3(charsetnum,maxlength):                                                     #An even smarter version of the the algorithm
    global found
    found = False
    global guess_count
    guess_count = 0
    charset = charset_list[charsetnum-1]                                                #The selected characters to try
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
            for char2 in charset:
                if l == 2:
                    if found == False:
                        guess_string = char2+char1
                        guess(guess_string)
                for char3 in charset:
                    if l == 3:
                        if found == False:
                            guess_string = char3+char2+char1
                            guess(guess_string)         
                    for char4 in charset:
                        if l == 4:
                            if found == False:
                                guess_string = char4+char3+char2+char1
                                guess(guess_string)
                        for char5 in charset:
                            if l == 5:
                                if found == False:
                                    guess_string = char5+char4+char3+char2+char1
                                    guess(guess_string) 
    if found == False:
        print('Password not found.')

def crack_help():
    print('Character set 1 is all lowercase letters.')
    print('Character set 2 is all uppercase letters.')
    print('Character set 3 is all letters.')
    #print('Character set 1 is all lowercase letters.')

def c(charsetnum,maxlength):                    #Shortcut to crack_v4
    crack_v4(charsetnum,maxlength)

    
#charsetnum,maxlength = eval(input('Please enter the character set you want to use and the maximum length you wish to crack to. Type crack_help() for more information. '))

#crack_v4(charsetnum,maxlength)

crack_v4(4,5)



                            
