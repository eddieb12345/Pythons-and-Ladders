import hashlib

passhash = '10d6504f565957d01007060e403845c0'

length = 5

found = False

def guess(guess_string): 
    guess_hash = hashlib.md5(guess_string.encode('utf-8')).hexdigest()
    if guess_hash == passhash:
        print('The password is ' + guess_string)
        global found
        found = True

for i in range(length):
    l = i+1
    for n in range(97,123):
            if l == 1:
                guess_string = chr(n)
                guess(guess_string)
                if found == True:
                    break
            elif l == 2:
                for m in range(97,123):
                    guess_string = chr(m)+chr(n)
                    guess(guess_string)
                    if found == True:
                        break
                if found == True:
                    break
            elif l == 3:
                for m in range (97,123):
                    for o in range(97,123):
                        guess_string = chr(o)+chr(m)+chr(n)
                        guess(guess_string)
                        if found == True:
                            break
                    if found == True:
                        break
                if found == True:
                    break            
            elif l == 4:
                for m in range (97,123):
                    for o in range(97,123):
                        for p in range(97,123):
                            guess_string = chr(p)+chr(o)+chr(m)+chr(n)
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
                for m in range (97,123):
                    for o in range(97,123):
                        for p in range(97,123):
                            for q in range(97,123):
                                guess_string = chr(q)+chr(p)+chr(o)+chr(m)+chr(n)
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

