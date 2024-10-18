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
