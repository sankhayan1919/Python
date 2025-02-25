def add(num1,num2):
  return num1+num2
def sub(num1,num2):
  return num1-num2
def mul(num1,num2):
  return num1*num2
def div(num1,num2):
  return num1/num2
calculator_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
  num1=int(input("enter first number: "))
  continue_flag=True
  while continue_flag:
    print(calculator_dict)
    choice=input("enter second number: ")
    num2=int(input('enter second number: '))
    calculator_function=calculator_dict[choice]
    result=calculator_function(num1,num2)
    print(result)
    continuation=input("'yes' for continue with result, 'no' for new calculation, 'exit' for exit:\n")
    if continuation=='yes':
      num1==result
    elif continuation=='no':
      continue_flag=False
      calculator()
    else:
      continue_flag=False
calculator()