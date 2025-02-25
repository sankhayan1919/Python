import random
def game():
  print("~"*41)
  print("Welcome to my Avengers Jumble Bumble Game")
  print("~"*41)
  words_easy=["ironman","thor","hulk","vision","antman","rocket","groot","thanos","loki","falcon","wasp","drax","wong","nebula","gamora","jarvis","ultron"]
  words_medium=["hawkeye","starlord","nickfury","spiderman","warmachine","blackwidow","deadpool","redskull","friday","hankpym","auntmay"]
  words_hard=["captainamerica","doctorstrange","pepperpotts","blackpanther","scarletwitch","wintersoldier","captainmarvel","howardstark"]
  level=input("Choose a level easy/medium/hard: ")
  if level=='easy':
    word=random.choice(words_easy)
    jumble=" ".join(random.sample(word,len(word)))
  elif level=='medium':
    word=random.choice(words_medium)
    jumble=" ".join(random.sample(word,len(word)))
  else:
    word=random.choice(words_hard)
    jumble=" ".join(random.sample(word,len(word)))
  print(jumble)
  guess=input("enter your guess: ").lower()
  if guess==word:
    print("You guessed right")
  else:
    print(f"The word is {word}")
    print("You guessed wrong")
  continuation=input("If you want to continue type 'yes' else type 'no': ")
  if continuation=='yes':
    game()
  else:
    print("Thanks! i hope you have enjoyed the game.")
    rate=input("Please enter * from 1 to 5 to rate my game:")
game()