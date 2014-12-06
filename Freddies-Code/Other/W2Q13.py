[x1,y1] = eval(input('Please input a first set of coordinates x,y: '))
[x2,y2] = eval(input('Please input a second set of coordinates x,y: '))

import math

def points(x1,y1,x2,y2):
    if x1!=x2:
        gradientOfLine = (y1-y2)/(x1-x2)
        coefficientOfLine = y1 - gradientOfLine*x1
    else:
        gradientOfLine = 'inf'
        coefficientOfLine = x1
    distanceBetween= math.sqrt((x1-x2)**2+(y1-y2)**2)
    return [distanceBetween,gradientOfLine,coefficientOfLine]


if x1==x2 and y1==y2:
    equationOfLine = 'There is no line.'

if gradientOfLine == 'inf':
    equationOfLine ='


equationOfLine

print('The distance between the points is',points(x1,y1,x2,y2)[0])   
    
print('The equation of the line is ' + equationOfLine)




             
