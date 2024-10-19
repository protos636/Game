from gameparts import Game
from gameparts.exceptions import FieldIndexError, SameFieldError


def main():
    gamer = Game()
    current_player = 'X'
    running = True
    while running:
        row, column = input_mark(gamer)
        print(f'Ход делает {current_player}')
        gamer.make_move(row, column, current_player)
        if gamer.check_win(current_player):
            print(f'player {current_player} won')
            running = False
        if gamer.is_board_full():
            print('Its a draw. Game board is full.')
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


if __name__ == '__main__':
    main()

