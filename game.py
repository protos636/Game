from gameparts import Game
from gameparts.exceptions import FieldIndexError, SameFieldError


def main():
    gamer = Game()
    current_player = 'X'
    running = True
    while running:
        print(f'Ход делает {current_player}')
        row, column = input_mark(gamer)
        gamer.make_move(row, column, current_player)
        if gamer.check_win(current_player):
            status = f'player {current_player} won\n'
            save_result(status)
            print(f'player {current_player} won')
            running = False
        if gamer.is_board_full():
            status = 'Its a draw\n'
            save_result(status)
            running = False
        gamer.print_board()
        current_player = 'O' if current_player == 'X' else 'X'


def input_mark(gamer):
    while True:
        try:
            row = int(input('Номер строки'))
            column = int(input('Номер столбца'))
            if row < 0 or row >= Game.field_size:
                raise FieldIndexError
            if column < 0 or column >= Game.field_size:
                raise FieldIndexError
            if gamer.board[row][column] != ' ':
                raise SameFieldError
        except Exception as e:
            print(f'{e}')
            continue
        except SameFieldError:
            print('Ячейка занята, введите другой знак')
            continue
        else:
            break
    return row, column

def save_result(player):
    file = open('results.txt', 'a')
    file.write(player)
    file.close()

if __name__ == '__main__':
    main()

