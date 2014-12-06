import requests

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()
print(WORDS)









print('Welcome to hangman and word guessing!')

word = 'chalfont'


length = len(word)
print('The number of letters in this word is',length)
lst1 = list(word)
lst2 = sorted(lst1)



def hangman(word):
  
  lst_success = []
  lst_success1 = sorted(lst_success)
  lst_failed = []
  lst_failed2 = sorted(lst_failed)
  guess2 = 3
  count_w = 0
  count_s = 0
  
  diff = int(input('Enter a difficulty 1, 2 or 3 in ascending difficulty:'))
  if diff == 3:
    guess1 = length +1
    print('You have ' + str(guess1) + ' guesses')

  elif diff == 2:
    guess1 = length +2
    print('You have ' + str(guess1) + ' guesses')

  elif diff == 1:
    guess1 = length + 3
    print('You have ' + str(guess1) + ' guesses')

    

  
  gameover = False
  while guess1>1 and gameover==False:
    letter = input('Guess a letter:')

    
    if len(str(letter)) > 1:
      print('That is not a letter you cheat...')



    elif letter in word:
      count_s+=1
      guess1-=1
      guess3 = guess1  
      lst_success.append(letter)
      print('CONGRATULATIONS, that\'s correct!')
      print('Guesses remaining:',guess3)
      print('Correct letters so far:',''.join(lst_success))
      lst_success1 = sorted(lst_success)
      
      

    else:
      count_w+=1
      count_s+=1
      guess1-=1
      guess3 = guess1 
      lst_failed.append(letter)
      print('BAD LUCK, that\'s incorrect, try again...')
      print('Guesses remaining:',guess3)
      print('Incorrect letters so far:',''.join(lst_failed))

      

    if lst_success1 == lst2 and gameover == False:
      print('CONGRATULATIONS, you have successfully guessed all the letters in the word!')
      print('You took a total of ' + str(count_s) + ' guesses to guess a ' + str(length) + ' letter word.')
      while guess2>0 and gameover == False:
        guess2-=1
        word1 = input('Enter the word these letters spell:')
        
        if word1 == word:
          print('CONGRATULATIONS, that is the correct word.')
          gameover = True
          
        else:
          print('That is incorrect, try again')
          print('Guess remaining:',guess2)
        
        if len(str(word1)) < len(str(word)):
          print('The word is not long enough')

    if guess1 == 1:
      print('Bad luck, you failed')
      print('The word was ' + str(word))
    
        
    
  
   

  
      

hangman(word)
  
