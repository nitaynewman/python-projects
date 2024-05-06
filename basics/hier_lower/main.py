from art import h_l_logo, vs
from game_data import data
import random
# from replit import clear

def format_user(user):
  # formating the users data
  name = user["name"]
  description = user["description"]
  country = user["country"]
  return f"{name}, a {description} from {country}"



def check_answer(guess, a_follower, b_follower):
  # taking the num of followers and returns if guess is correct
  if a_follower > b_follower:
    return guess == "a"
  else:
    return guess == "b"


game = True
score = 0
print(h_l_logo)
user_b = random.choice(data)

while game:
  # getting a random ser from the db
  user_a = user_b
  user_b = random.choice(data)
  if user_a == user_b:
    user_b = random.choice(data)
  
  print(f"Compare A: {format_user(user_a)}")
  print(vs)
  print(f"Against B: {format_user(user_b)}")
  # leting the user guess a who has mor followers
  guess = input("guess who has more follower: A or B. \n") .lower()
  # going to the "is correct" function to find out if correct
  a_follower = user_a["follower_count"]
  b_follower = user_b["follower_count"]
  is_correct = check_answer(guess, a_follower, b_follower)
  # clear()
  print(h_l_logo)
  # returning feedback to user
  if is_correct:
    score += 1
    print(f"correct, your score is {score} \n \n")
  else:
    print(f"wrong, your fainal score: {score} \n \n")
    game = False