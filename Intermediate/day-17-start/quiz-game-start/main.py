from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

# ctrl + G to select next occurrence of variable
# shift+ ctrl + G to deselect next occurrence of variable
# ctrl + cmd + G to select all occurrences
# option + click to set multiple cursors in the editor
quiz = QuizBrain(question_bank)
quiz.next_question()
