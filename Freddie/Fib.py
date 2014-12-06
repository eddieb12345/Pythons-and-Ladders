def fib(number):
    prev=0
    curr=1
    for n in range(2,number+1):
        if number <= 20:
            print(curr)
        if number >= 100000:
            for i in range(1000):
                if n == int(0.001*i*number):
                    print(str(0.1*i) + '% done.')
        nxt=curr+prev
        prev=curr
        curr=nxt
    if len(str(curr))<= 100:
        print(curr)
    print('The number is ' + str(len(str(curr))) + ' digits long.')

fib_number=eval(input('Please enter a number: '))

fib(fib_number)


 
