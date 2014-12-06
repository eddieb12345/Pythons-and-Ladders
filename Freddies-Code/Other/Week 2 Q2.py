nameList = eval(input('Please enter a list of students. A list of those with names starting with the letters A-M will be printed. '))
for name in nameList:
    if name[0]<='M':
        print(name)
    
