import random
cinema=[
    {
        "Name":"Dangal",
        "Starcast":"Amir Khan",
        "collection":2024
    },
    {
        "Name":"RRR",
        "Starcast":"Jn.NTR, Ramcharan",
        "collection":1387
    },
    {
        "Name":"KGF 2",
        "Starcast":"Yash",
        "collection":1230
    },
    {
        "Name":"Bahubali 2",
        "Starcast":"Prabhas",
        "collection":1810
    },
    {
        "Name":"Pathaan",
        "Starcast":"Shahrukh Khan",
        "collection":1050
    },
    {
        "Name":"Jawan",
        "Starcast":"Shahrukh Khan",
        "collection":1148
    },
     {
       "Name":"PK",
       "Starcast":"Amir Khan",
       "collection":769
    },
    {
        "Name":"Bajarangi Bhaijaan",
        "Starcast":"Salman Khan",
        "collection":969
    },
    {
        "Name":"Animal",
        "Starcast":"Ranbir Kapoor",
        "collection":890
    },
    {
        "Name":"Salaar",
        "Starcast":"Prabhas",
        "collection":625
    },
    {
        "Name":"Gadar 2",
        "Starcast":"Sunny Deol",
        "collection":691
    },
    {
        "Name":"Secret Superstar",
        "Starcast":"Amir Khan",
        "collection":905
    },
    {
        "Name":"2.0",
        "Starcast":"Rajnikanth",
        "collection":699
    },
    {
        "Name":"Jailer",
        "Starcast":"Rajnikanth",
        "collection":610
    },
    {
        "Name":"Leo",
        "Starcast":"Thalapati Vijay",
        "collection":623
    },
    {
        "Name":"Sultan",
        "Starcast":"Salman Khan",
        "collection":615
    }

]
print("~"*37)
print("Welcome to Box-Office Collection Game")
print("~"*37)
def display(cinema):
  name=cinema["Name"]
  starcast=cinema["Starcast"]
  return (f"Name is '{name}' and starcast is '{starcast}'")

def check_answer(answer,collection1,collection2):
  if(collection1>collection2 and answer==1):
     print(f"You won!")  
  elif(collection1<collection2 and answer==2):
     print(f"You won!")
  elif(collection1==collection2 and (answer==1 or 2)):
    print("Its a draw.")
  else:
    print(f"You lose.")
    
def game():  
  cinema1=random.choice(cinema)
  print(f"compare1: {display(cinema1)}")
  print(f"VS")
  cinema2=random.choice(cinema)
  print(f"compare2: {display(cinema2)}")
  print("\nwhat do you think which movie have higher worldwide box office collection?\n")
  answer=int(input("Type 1 for cinema1, 2 for cinema2:\n"))
  collection1=cinema1["collection"]
  collection2=cinema2["collection"]
  print(f"Cinema1 collects {collection1} cr. rupees")
  print(f"Cinema2 collects {collection2} cr.rupees")
  check_answer(answer,collection1,collection2)  
  continuation=input("Do you want to play again?(yes/no): ").lower()
  if(continuation=="yes"):
      game()
game()