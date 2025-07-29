menu={
    "cappuccino": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "coffee": 25,
            "sugar": 20
        },
        "cost": 50,
    },
    "americano": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "sugar": 15,
            "coffee": 15
        },
        "cost": 45,
    },
    "espresso": {
        "ingredients": {
            "water": 100,
            "milk": 10,
            "sugar": 5,
            "coffee": 30
        },
        "cost": 35,
    },
    "iced coffee": {
        "ingredients": {
            "water": 100,
            "milk": 40,
            "coffee": 20,
            "sugar": 10,
            "ice": 25
        },
        "cost": 45,
    },
}
profit = 0
resources = {
    "water": 500,
    "milk": 400,
    "sugar": 500,
    "coffee": 200,
    "ice": 100
}
total=0

def check_resources(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item]>resources[item]:
      print(f"Sorry, there is not enough item")
      return False
  return True

def your_payment():
  return total
def coffee_cost():
  return coffee_type["cost"]

def coins():
  global total
  print("\nPlease insert coins")
  coins_five=int(input("\nhow many 5 rupees coin?"))
  coins_ten=int(input("how many 10 rupees coin?"))
  coins_twenty=int(input("how many 20 rupees coin?"))
  total=coins_five*5+coins_ten*10+coins_twenty*20
  return total

def payment_success(your_payment,coffee_cost):
  if(your_payment>=coffee_cost): 
    global profit
    profit=profit+coffee_cost
    change=your_payment-coffee_cost
    print(f"\nHere is your change: {change}rupees")
    return True
  else:
    print("\nSorry, this is not enough money\n\n")
    return False
  
def processor(coffee_name,order_ingredients):
    for item in order_ingredients:
      resources[item]=resources[item]-order_ingredients[item]
    print("\nWait a little bit, your coffee is processing..................., grab some snacks.\n")
    print(f"Here is you coffee: '{coffee_name}', Enjoy it!!\n")

machine_on=True
while machine_on:
  choice=input("\nWhat do you want?-\n\ncappuccino- 50rupees\namericano- 45rupees\nespresso- 35rupees\niced coffee- 45rupees\n\n'report' to know the quantity of the ingrediants and 'off' to switch of the machine:\n")
  if choice=="off":
    machine_on=False
  elif choice=="report":
    print(f"\nMoney = {profit}rupees\n")
    print(resources)
  else:
    coffee_type = menu.get(choice)
    if coffee_type:
        order_ingredients = coffee_type["ingredients"].copy()
        if check_resources(order_ingredients):
            total = coins()
            coffee_cost_value = coffee_cost()
            if payment_success(your_payment(),coffee_cost_value):
              processor(choice, order_ingredients)
    else:
        print("Invalid choice. Please select a valid coffee option.")
