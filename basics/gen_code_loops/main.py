import pandas

data = pandas.read_csv("file.csv")
# print(data.to_dict())

dictionery = {row.letter: row.code for (index, row) in data.iterrows()}
# print(f"your dict is {dictionery}")
def gen_code():
  word = input("enter your name: ").upper()
  try:
    output = [dictionery[letter] for letter in word]

  except KeyError:
    print('please enter only letters, not eny other car')
    gen_code()
  else:
    print(output)

gen_code()
# student_dict = {
#   "student": ["Angela", "James", "Lily"], 
#   "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#   #Access key and value
#   pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#   #Access index and row
#   #Access row.student or row.score
#   pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

