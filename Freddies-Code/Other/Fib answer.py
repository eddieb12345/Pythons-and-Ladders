
# Practical 4 Question 1

def fib(i):
    'returns the ith Fibonacci number'
    previous = 1	# 0th Fibonacci number
    current = 1	        # 1st Fibonacci number
    num_generated = 1   # which Fibonacci number generated so far?
    while i > num_generated: # keep going until ith number generated
        previous, current = current, previous + current
        num_generated = num_generated + 1
    return current

i = int(input('Give me the ith Fibonacci number you want to generate (i >= 1): '))
ith = fib(i - 1)  # so the 1st number is fib(0), etc.
print('The {0}th Fibonacci number is {1}'.format(i,ith))
