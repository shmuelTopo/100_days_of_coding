class QuizBrain:
    def __init__(self, questions_list):
        self._questions_list = questions_list
        self._question_num = 0
        self.score = 0

    def next_question(self):
        question = self._questions_list[self._question_num]
        answer = input(f'q {self._question_num + 1}. '
                       f'{question.text} (True/False)? ')

        self.check_answer(answer, question.answer)
        self._question_num += 1

    def still_has_questions(self):
        return len(self._questions_list) > self._question_num

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('That\'s wrong!')
        print(f'The correct answer is {correct_answer}')
        print(f'Your current score is {self.score}/{len(self._questions_list)}\n')
