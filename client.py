from truth_or_false.game import Game
from truth_or_false.game_status import GameStatus

print('Welcome to my gameY you will be asking questions one by one. In case you will not make more mistakes than you '
      'allowed to make, you will win. Otherwise you will loose!\n\n')

game = Game()
game.get_data()

while game.status == GameStatus.STARTED:
    print('The question is:')
    print(game.ask_question())
    if game.answer_question(input('\nEnter your answer "y"/"n": ')):
        print('Right answer!', game.correct_answer())
    else:
        print('Yow were close!', game.correct_answer())
    print('\n')

if game.won:
    print('Congratulations!')

else:
    print('You lost!')