rate = eval(input('Please input the hourly rate: '))

hours = eval(input('Please input the number of hours worked: '))

pay = rate*min(hours,40)+1.5*rate*max(hours-40,0)

print('The employee should be payed £'+str(pay))



    



             
