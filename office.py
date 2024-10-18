class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля'

class SameFieldError(IndexError):

    def __str__(self):
        return 'В этой ячейке уже стоит знак'

class Game:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(self.field_size)]
                      for _ in range(self.field_size)]

    def print_board(self):
        for i in self.board:
            print('|'.join(i))
            print('-' * 5)

    def make_move(self, x, y, mark):
        if x >= 0 and y >= 0:
            self.board[x][y] = mark

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
    
    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] != ' ':
                    continue
                else:
                    return False
        return True
        
    def check_win(self):
        is_win = False
        counter = 0
        for row in range(self.field_size):
            for column in range(self.field_size - 2):
                if ((self.board[row][column] == self.board[row][column + 1]) and
                   (self.board[row][column + 1] == self.board[row][column + 2])):
                       print(self.board[row][column])
        print(counter)
        return is_win    

def main():
    gamer = Game()
    current_player = 'X'
    running = True
    while running:
        gamer.print_board()
        print(f'Ход делает {current_player}')
        x, y = input_mark(gamer)
        gamer.make_move(x, y, current_player)
        current_player = 'O' if current_player == 'X' else 'X'
        gamer.print_board()
        if gamer.is_board_full():
            print('Its a draw. Game board is full.')
            break
        if gamer.check_win():
            print('player win')
            break
        
        
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
