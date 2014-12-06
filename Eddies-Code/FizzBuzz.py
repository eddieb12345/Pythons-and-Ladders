num = eval(input('Enter a number:'))


line = []
for num in range(1,num+1):
  if num%3 == 0 and num%5 == 0:
    line.append("Fizz Buzz")
  elif num%3 == 0:
    line.append("Fizz")
  elif num%5 == 0:
    line.append("Buzz")
  else:
    line.append(num)

for numbers in line:
  print(numbers)
