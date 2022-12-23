#Calculator 
import art

def add(number_1, number_2):
  return number_1 + number_2

def subtract(number_1, number_2):
  return number_1 - number_2

def multiply(number_1, number_2):
  return number_1 * number_2

def divide(number_1, number_2):
  return number_1 / number_2

operations = {
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide
}

def calculator():
  print(art.logo)
  
  n1 = float(input("What's the first number?: "))
  for symbols in operations:
    print(symbols)
  s_continue = True
  
  while s_continue:
    operation_choice = input("Select an operation : ")
    n2 = float(input("What's the following number?: "))
    calc_function = operations[operation_choice]
    f_results = calc_function(n1, n2)
    
    print(f"{n1} {operation_choice} {n2} = {f_results}")
    
    if input(f"Type 'y' to continue calculating with {f_results}, or type 'n' to start a new calculation.: ") == 'y':
      n1 = f_results
    else:
      s_continue = False
      calculator()

calculator()


  

