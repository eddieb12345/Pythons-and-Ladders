import turtle

def polygon(n):
    for i in range(0,n):
        turtle.forward(360/n)
        turtle.left(360/n)
    
integer = eval(input('Please input an integer >= 3: '))

polygon(integer)
