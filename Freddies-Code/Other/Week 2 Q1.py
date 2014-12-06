list = eval(input('Please input a list. The string "secret" will not be printed. '))
for item in list:
    if item != 'secret':
        print(item)
