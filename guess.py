import random

num=random.randint(1,100)
print(num)
print("Welcome to the Guessing Game!")
print("I'm thinking a number between 1 and 100")

difficulty=input("Choose your difficulty: ").lower()
if difficulty=="easy":
  turn=10
elif difficulty=="hard":
  turn=5
else:
  print("Wrong input")

while turn>0:
  print(f"\nYou have {turn} attempts remaining to guess the number")
  guess=int(input("Make a guess: "))
  if guess==num:
    print(f"You got it! The number was {num}.")
    turn=-1
  elif guess>num:
    print("Too High")
    turn-=1
  elif guess<num:
    print("Too Low")
    turn-=1
if turn==0:
  print("You've run out of guesses, You Lose.....")
