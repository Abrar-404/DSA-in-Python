n = 5

def Fibonacci(n):
  if (n == 0 or n == 1):
    return 1
  else:
    result = Fibonacci(n - 1) + Fibonacci(n - 2)
    return result
  

value = Fibonacci(n)
print(f"The {n}th Fibonacci number is: {value}")