import math

def heron(n,x0,error):
    xcur = x0
    xprev = 0
    while math.fabs(xcur-xprev) > error:            #Checks if the difference between two guesses is within the error bound
        xprev = xcur
        xcur = 0.5*(xcur + n/xcur)                  #Applies the heron method
        print(xcur)
    print('The heron method guessed: ' + str(xcur))
    print('The math value is: ' + str(math.sqrt(n)))

inputs =eval(input('Please enter the number you wish to find the sqaure root of,'\
             ' an arbitray guess and an error bound in the form'\
             ' [number,guess,error]: '))

[number,guess,error] = inputs
            
heron(number,guess,error)
        
    
