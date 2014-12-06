def bubble_sort(lst):                                               #Bubble sort from left to right          
    print(lst)
    n= len(lst)-1                                                   #Converts the list length to index numbers
    done = False                    
    while done == False:                                            #Checks if the sort has finished
        done = True                                                 #Assumes the sort is completed
        for i in range(n):      
            if lst[i] > lst[i+1]:                                   #Compares the two values
                done = False                                        #If they aren't in order, the sort isn't finished
                lst[i],lst[i+1] = lst[i+1],lst[i]                   #Swaps the values   
                print(lst)          
        i = 0                                                       #Resets the counter so the sort can be repeated


def selection_sort(lst):                                            #Selection sort starting with smallest value
    print(lst)
    n=len(lst)                                                      #Converts the list length to index numbers
    finished = 0                                                    #Number of values that have been sorted
    while finished<n:                                               #Checks if all the values have been sorted
        for i in range(n):                                          #Iterates through the indexes to compare in the list
            selection_index = i                                         
            for j in range(finished,n):                             #Iterates through the indexes to compare to in the list
                if lst[selection_index] > lst[j]:                   #Compares the two values
                    selection_index = j                             #Replaces the selection index with the value index if the value is smaller
            lst.insert(finished,lst.pop(selection_index))           #Removes the selected value
            finished = finished + 1                                 #Places the selected value after the other sorted values
            print(lst)
            

sample = [1,4,5,9,3,6,6,1,3,1,5,7,8,4,1,2,4,8,9,5,3,1,3,4,5,7]

bubble_sort(sample)

#selection_sort(sample)
            
            
            
            
