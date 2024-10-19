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

    def check_win(self, player):
        res = False
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                res = True
        for i in range(3):
            if (self.board[0][0] == self.board[1][1] == self.board[2][2] ==
                player or
                    self.board[0][2] == self.board[1][1] == self.board[2][0] ==
                    player):
                res = True
        return res