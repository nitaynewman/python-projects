class QuizzBrain:
  def __init__(self, q_list):
    self.question_num = 0
    self.question_list = q_list
    self.score = 0

  def next_Q(self):
    current_question = self.question_list[self.question_num]
    self.question_num += 1
    Query = input(f"Q.{self.question_num}: {current_question.text} (True/False): ")
    self.check_answer(Query, current_question.answer)


  def end_quiz(self, q_list):
    return self.question_num < len(self.question_list)
    # num_Q = len(q_list)
    # if self.question_num > num_Q:
    #   return False
    # else:
    #   print("end of the quiz")

  def check_answer(self, Query, currect):
    if currect.lower() == Query.lower():
      self.score += 1
      print("you r write")
      
    else:
      print("u r wrong")
      print(f"the write answer was {currect}")
    print(f"your score is {self.score}/{self.question_num}")
    