from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for q in question_data:
  question_text = q["text"]
  question_answer = q["answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)


Quiz = QuizzBrain(question_bank)

while Quiz.end_quiz:
  Quiz.next_Q()
print("u reached the end of the game")