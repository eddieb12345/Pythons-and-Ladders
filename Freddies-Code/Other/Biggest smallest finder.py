#def efficiency_calc(comparisons,length):
#    n = length
#    a = comparisons//n                          #Takes the whole part of the division
#    b = comparisons%n                            #Takes the remainder of the division
#    print('The solution was found in ' +\
#          str(a) + 'n + ' + str(b) + 'comparison.')

def select_biggest(lst):                        #Finds the biggest number in n-1 comparisons
    biggest_index = sample[0]                   #The index of the biggest number
    comparisons = 0
    for i in range(1,len(lst)):
        if lst[i]>lst[biggest_index]:
            biggest_index=i
        comparisons += 1
    print('The biggest is ' + str(lst[biggest_index]))
    print(str(comparisons) + ' comparisons were made.')
        
def select_biggest_smallest(lst):               #Finds the biggest number in n-3 comparisons        
    biggest_index = sample[0]                   #The index of the biggest number
    smallest_index = sample[0]                  #The index of the samllest number
    comparisons = 0
    for i in range(1,len(lst)):                 
        if lst[i]>lst[biggest_index]:           #Compares each value to the biggest
            biggest_index=i                     #Records the index of the new biggest number
        comparisons += 1
    for i in range(1,biggest_index):            #Compares the first half of the list, excluding the biggest number
        print(i)
        if lst[i]<lst[smallest_index]:          #Compares each value to the smallest
            smallest_index=i                    #Records the index of the new samllest number
        comparisons += 1
    for i in range(biggest_index+1,len(lst)):   #Compares the second half of the list, excluding the biggest number
        print(i)
        if lst[i]<lst[smallest_index]:          #Compares each value to the smallest
            smallest_index=i                    #Records the index of the new samllest number
        comparisons += 1
    print('The biggest is ' + str(lst[biggest_index]))
    print('The smallest is ' + str(lst[smallest_index]))
    print(str(comparisons) + ' comparisons were made.')

def select_biggest_2ndbiggest(lst):
    biggest_index = sample[0]                   #The index of the biggest number
    second_biggest_index = sample[0]            #The index of the second biggest number
    comparisons = 0
    for i in range(1,len(lst)):
        comparisons += 1
        if lst[i]>lst[biggest_index]:
            biggest_index=i   
        else:
            comparisons += 1    
            if lst[i]>lst[second_biggest_index]:
                second_biggest_index=i
    print('The biggest is ' + str(lst[biggest_index]))
    print('The second biggest is ' + str(lst[second_biggest_index]))    
    print(str(comparisons) + ' comparisons were made.')
    
sample = [2,6,7,3,56,8,23,12,57,97,23,56,8,12,4,3,6,98,3,2,4,5,6,7,8,5,4,2,56]

#select_biggest_2ndbiggest(sample)
