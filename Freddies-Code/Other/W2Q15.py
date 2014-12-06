[X1,Y1,R1] = eval(input('Please enter the x,y coordinates and radius of the first circle: '))
[X2,Y2,R2] = eval(input('Please enter the x,y coordinates and radius of the second circle: '))

import math

def collision(x1,y1,r1,x2,y2,r2):
    if math.sqrt((x1-x2)**2+(y1-y2)**2)<=r1+r2:
        print('They collide.')
    else:
        print('They do not collide.')

collision(X1,Y1,R1,X2,Y2,R2)

    
    
    

