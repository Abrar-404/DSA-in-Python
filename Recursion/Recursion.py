n = 5

def Recursion(n):
  if (n == 0 or n == 1):
    return 1
  else:
    result = n * Recursion(n - 1)
    return result
  
  
Value = Recursion(n)
print(f"The factorial of {n} is {Value}")