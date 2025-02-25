import random
AMETEUR_LEVEL_ATTEMPTS=15
EASY_LEVEL_ATTEMPTS=10
MEDIUM_LEVEL_ATTEMPTS=7
HARD_LEVEL_ATTEMPTS=5
EXPERT_LEVEL_ATTEMPTS=3
def difficulty(level):
  if(level=='expert'):
    print("you have 3 attempts\n")
    return EXPERT_LEVEL_ATTEMPTS
  elif(level=='hard'):
    print("you have 5 attempts\n")
    return HARD_LEVEL_ATTEMPTS
  elif(level=='medium'):
    print("you have 7 attempts\n")
    return MEDIUM_LEVEL_ATTEMPTS
  elif(level=='easy'):
    print("you have 10 attempts\n")
    return EASY_LEVEL_ATTEMPTS
  elif(level=='ameteur'):
    print("you have 15 attempts\n")
    return AMETEUR_LEVEL_ATTEMPTS
  else:
    raise ValueError("invalid input")
    return
   
def check_answer(answer,guessed_number,attempts):
  if(guessed_number>answer):
    print("your guess is high")
    return attempts-1
  elif(guessed_number<answer):
    print("your guess is low")
    return attempts-1
  else:
    print("Congratulations!!you have guessed right")
    print("Thanks! i hope you have enjoyed the game.")
    rate=input("Please enter * to rate my game:")

def game():
   print("~"*27)
   print("Welcome to my Guessing Game")
   print("~"*27)
   print("Guess a number between 1 to 100")
   answer=random.randint(1,100)
   level=input("enter your level (ameteur/easy/medium/hard/expert):")
   attempts=difficulty(level)
   guessed_number=0
   while guessed_number!=answer:
     print(f"you have now {attempts} attempts only")
     guessed_number=int(input("enter your guess:  "))
     attempts=check_answer(answer,guessed_number,attempts)
     if(attempts==0):
       print("you lose")
       print(f"The right answer is {answer}")
       print("Thanks! i hope you have enjoyed the game.")
       rate=input("Please enter * from 1 to 5 to rate my game:")
       break
     elif(guessed_number!=answer):
       print("guess again")
     else:
       return
game()

