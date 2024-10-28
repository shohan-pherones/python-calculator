def add(a, b):
  """Returns the sum of a and b."""
  return a + b

def subtract(a, b):
  """Returns the difference between a and b."""
  return a - b

def multiply(a, b):
  """Returns the product of a and b."""
  return a * b

def divide(a, b):
  """Returns the division of a by b. Handles division by zero."""
  if b != 0:
    return a / b
  else:
    return "Error: Cannot divide by zero"

def calculator():
  print("Simple Calculator")
  print("Operations: +, -, *, /")

while True:
  num1 = float(input("Enter the first number: "))
  operation = input("Enter operation (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operation.")
    continue

  print(f"Result: {result}")

  again = input("Do you want to perform another calculation? (yes or no): ").lower()
  if again != "yes":
    break

calculator()