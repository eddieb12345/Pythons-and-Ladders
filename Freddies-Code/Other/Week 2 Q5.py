number = eval(input('Enter a positive integer. All positive divisors will be printed. '))

for n in range (1,number+1):
    if number%n==0:
        print(n)

