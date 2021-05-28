from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(i["text"], i["answer"]) for i in question_data]

quiz_game = QuizBrain(question_bank)

while quiz_game.still_has_questions():
    quiz_game.next_question()

print(f'You completed the quiz your final score is {quiz_game.score}/{len(question_bank)}')

