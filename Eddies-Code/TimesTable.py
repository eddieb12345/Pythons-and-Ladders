import datetime

n = int(input('Enter a number you would like the timestable of:'))

def timestable(n):
    if len(str(n)) >= 5:
        answer = input('This will take a while, are you sure you want this number?')
        if answer.lower() == 'yes':
            time4 = datetime.datetime.now()
            for i in range(0,n+1):
                print(str(n) +' x ' + str(i) + ' = ' + str(n*i))
            time5 = datetime.datetime.now()
            time6 = time5 - time4
            print('The time taken to execute was,',time6)
            print('I told you...')
        else:
            n1 = int(input('Enter another number you would like the timestable of:'))
            time7 = datetime.datetime.now()
            for i in range(0,n1+1):
                print(str(n1) +' x ' + str(i) + ' = ' + str(n1*i))
            time8 = datetime.datetime.now()
            time9 = time8 - time7
            print('The time taken to execute was,',time9)
    else:
        time1 = datetime.datetime.now()
        for i in range(0,n+1):
            print(str(n) + ' x ' + str(i) + ' = ' + str(n*i))
        time2 = datetime.datetime.now()
        time3 = time2 - time1
        print('The time taken to execute was,',time3)

timestable(n)




