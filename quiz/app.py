from print_color import print
from data import quizzes


# module =  {
#       "name": "Basics of Python",
#       "questions": [
#         {
#           "question": "What is the correct file extension for Python files?",
#           "options": ["a) .py", "b) .pt", "c) .pyt", "d) .python"],
#           "answer": "a"
#         },
#         {
#           "question": "Which of the following is a valid variable name in Python?",
#           "options": ["a) 2name", "b) name2", "c) -name", "d) name-"],
#           "answer": "b"
#         },
#         {
#           "question": "What is the output of the following code? print(2 * 3 + 4)",
#           "options": ["a) 14", "b) 10", "c) 24", "d) 8"],
#           "answer": "b"
#         }
#       ]
#     }

score = 0
total = 0

def take_user_input():
    user_input = input("Enter you answer ")
    if user_input not in ["a","b","c","d"]:
        print("Invalid option, select a,b,c or d")
        take_user_input()
    else:
        return user_input


for qmodule in quizzes:

    print("Module Name:" , qmodule["name"] ,color='green', format='underline', background='grey' )

    #Loop on each question
    for quiz in qmodule['questions']:
        #Print the question and options
        print(quiz["question"], color='cyan')
        print("Oprions:", color="yellow")
        for option in quiz['options']:
            print(option, background="blue")

        #Take input from user
        #Validate user input [a,b,c,d]
        user_input = take_user_input()
        
        #check the answer and update the score
        if user_input == quiz['answer']:
            score += 1
        total += 1


print("Quiz Completed", color="green")

if score == 0:
    print(f"Your Score is {score}/{total}", color="red")
else:
    print(f"Your Score is {score}/{total}", color="green")
#finally print the score