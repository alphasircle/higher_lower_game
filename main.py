from replit import clear
import random
from game_data import data
from art import logo, vs

# takes dictionary from a_value or b_value list and 
# creates list of values needed for printing info in console for user
def extract_value(value_from_key):
  value_list = []
  for key in value_from_key:
    if key != 'follower_count':
      value_list.append(value_from_key[key])
  return value_list

# adds 1 point to score, if the answer is right, else game lost and prints final score.
# also returns string, to stop while isinstance(score, int) loop
score = 0
def compare(first_value, second_value, guess):
  if guess == "A" and first_value['follower_count'] > second_value['follower_count']:
    return score + 1
  elif guess == "B" and first_value['follower_count'] < second_value['follower_count']:
    return score + 1
  else:
    return f"Wrong. Final score: {score}\n"

# assigns B to A and B receives new value, also prevents A == B
def shift(shift_a, shift_b):
  shift_a = shift_b
  while shift_a == shift_b:
    shift_b = data[random.randrange(len(data) - 1)]
  new_a_b_value = [shift_a, shift_b]
  return new_a_b_value

# start with 2 random values and below that while checks to prevent A == B
a_value = data[random.randrange(len(data) - 1)]
b_value = data[random.randrange(len(data) - 1)]

while a_value == b_value:
  a_value = data[random.randrange(len(data) - 1)]
  b_value = data[random.randrange(len(data) - 1)]

# checks if score is int type to keep game going, score can be string, because of compare() function
while isinstance(score, int):
  
  extracted_list_a = extract_value(a_value) # list to print values to console
  extracted_list_b = extract_value(b_value)

  print(logo + "\n") 
  print(f"Compare A: {extracted_list_a[0]}, a {extracted_list_a[1]}, from {extracted_list_a[2]}\n")
  print(vs + "\n")
  print(f"Compare B: {extracted_list_b[0]}, a {extracted_list_b[1]}, from {extracted_list_b[2]}\n")

  # starts to display when user scores first point
  if score > 0:
    print(f"Right answer. Score: {score}\n")
  
  take_a_guess = input('Who has more followers? Type "A" or "B"\n').upper() # input for compare()
  score = compare(a_value, b_value, take_a_guess) # assigns int to raise score or string to end game

  # checks if score is int, if yes, assigns new A and B value, if not ends game
  if isinstance(score, int):
    clear()
    new_a_b_value_list = shift(a_value, b_value) # takes list from shift() with new A and B values
    a_value = new_a_b_value_list[0] # assign new A value from new_a_b_value_list
    b_value = new_a_b_value_list[1] # assign new B value from new_a_b_value_list
  else:
    clear()
    print(score)








    
    
  


