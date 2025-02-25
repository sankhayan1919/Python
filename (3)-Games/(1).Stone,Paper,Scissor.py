import random
print("****************************************\nWelcome to my stone, paper, scissor game\n****************************************")

def game():
  your_choice=str(input("enter among 's' for scissor, 'r' for rock and 'p' for paper: "))
  choice=['r','s','p']
  comp_choice=random.choice(choice)
  if(your_choice=='s' and comp_choice=='p') or (your_choice=='r' and comp_choice=='s') or (your_choice=='p' and comp_choice=='r'):
    print(f"computer choice is: {comp_choice}")
    print('You win')
  elif(your_choice=='p' and comp_choice=='s') or (your_choice=='s' and comp_choice=='r') or (your_choice=='r' and comp_choice=='p'):
    print(f"computer choice is: {comp_choice}")
    print('you lose')
  else:
    print(f"computer choice is: {comp_choice}")
    print('draw')
  continuation=input("If you want to continue type 'yes' else type 'no': ")
  if continuation=='yes':
    game()
  else:
    print("Thanks! i hope you have enjoyed the game.")
    rate=input("Please enter * from 1 to 5 to rate my game:")
game()