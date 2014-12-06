sentence = input('Please enter an English sentence: ')

def average(SENTENCE):

    words = SENTENCE.split(' ')

    sum = 0

    while '' in words:              #Removes empty spaces
        words.remove('')

    for word in words:              #Counts the total length
        sum = sum + len(word)

    avg = sum/len(words)            #Calculates the average length

    return avg
    
print('The average world length of your string is ' + str(average(sentence)))

