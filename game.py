from truth_or_false.exceptions import InvalidOperationError
from truth_or_false.game_status import GameStatus


class Game:

    def __init__(self, filename: str = './data/Questions.csv', max_mistakes: int = 3):
        self.__filename = filename
        self.__max_mistakes = max_mistakes
        self.__mistakes = 0
        self.__status = GameStatus.NOT_STARTED
        self.__questions = []
        self.__current = []
        self.__questionNumber = 0
        self.__quantity = 0

    def get_data(self):
        with open(self.filename, 'r', encoding='utf8') as file:
            for line in file:
                self.questions.append(line.split(';'))
        self.__status = GameStatus.STARTED
        self.__quantity = len(self.questions)

    def ask_question(self):

        if not self.status == GameStatus.STARTED:
            raise InvalidOperationError(f'Not appropriate game status. Current: {self.status}')

        self.__current = self.questions[self.question_number]
        self.__questionNumber += 1
        return self.current[0]

    def answer_question(self, answer):
        answer = 'Yes' if answer == 'y' else 'No'
        if self.current[1] == answer:
            self.in_game()
            return True
        self.__mistakes += 1
        self.in_game()
        return False

    def correct_answer(self):
        return self.current[2]

    def in_game(self):
        if self.mistakes == self.max_mistakes:
            self.__status = GameStatus.LOST

        elif self.question_number == self.quantity:
            self.__status = GameStatus.WON

    @property
    def won(self):
        return True if self.status == GameStatus.WON else False

    @property
    def filename(self):
        return self.__filename

    @property
    def max_mistakes(self):
        return self.__max_mistakes

    @property
    def mistakes(self):
        return self.__mistakes

    @property
    def status(self):
        return self.__status

    @property
    def questions(self):
        return self.__questions

    @property
    def current(self):
        return self.__current

    @property
    def question_number(self):
        return self.__questionNumber

    @property
    def quantity(self):
        return self.__quantity
