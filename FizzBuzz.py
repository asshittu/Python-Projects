#FizzBuzz Project

for fizz in range(1, 101):
  if fizz % 3 == 0 and fizz % 5 == 0:
    print("FizzBuzz")
  elif fizz % 3 == 0:
    print("Fizz")
  elif fizz % 5 == 0:
    print("Buzz")
  else:
    print(fizz)
