# Quiz Application

# Classes: Question, Quiz.

# Load questions from a file, keep score.

# Practice file handling + OOP



class Question:
  def __init__(self ,  text , options , correct_index):
    self.text = text
    self.options = options
    self.correct_index = correct_index

  def check_ans(self , user_choice):
    """If user_choice match the correct answer"""
    return user_choice == self.correct_index


class Quizz:
  def __init__(self):
    self.questions = []
    self.score = 0

  def load_question(self , filename):
    """Load Question from a file"""
    with open("question.txt" , "r")as file:
      for line in file:
        parts = line.strip().split(",")
        text = parts[0]
        options = parts[1:-1]
        correct_index = int(parts[-1])
        question = Question(text , options , correct_index)
        self.questions.append(question)

  def start(self):
    """Run the quiz game"""
    for i , question in enumerate(self.questions, start = 1):
        print(f"\nQ{i}: {question.text}")
        for idx , option in enumerate(question.options , start = 1):
          print(f"{idx}.{option}")

        # Get answer from the user
        choice = int(input("Your choice(1-4): "))
        if question.check_ans(choice):
          print("Correct")

          self.score += 1
        else:
          print("Wrong")
    print(f"\n Final score : {self.score}/{len(self.questions)}")


if __name__ == "__main__":
  quiz = Quizz()
  quiz.load_question("questions.text")
  quiz.start()











