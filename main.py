question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The first computer bug was formed by faulty wires.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "AMD created the first consumer 64-bit processor.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    }
]
#question_data = [
#    {"text": "A slug's blood is green.", "answer": "True"},
#    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
#             " you are free to take it home to eat.", "answer": "True"},
#    {"text": "In London, UK, if you happen to die in the House of Parliament,"
#             " you are entitled to a state funeral.", "answer": "False"},
#    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
#]
###########################################
class Question: # class Name
    def __init__(self,q_text,q_answer): # Initialization Constructor;
        self.text=q_text
        self.answer=q_answer
# When Create Object From class Variables initialized;
###########################################
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def still_has_questions(self):#return True or return False.
        return self.question_number<len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong.")
        print(f"The Correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
###########################################
#from question_model import Question
#from data import question_data
#from quiz_brain import QuizBrain
###########################################
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
##########################################
