from gameparts import Game
from gameparts.exceptions import FieldIndexError


def main():
    gamer = Game()
    while True:
        try:
            row = int(input('Номер строки'))
            column = int(input('Номер столбца'))
            if row < 0 or row >= Game.field_size:
                raise FieldIndexError
            if column < 0 or column >= Game.field_size:
                raise FieldIndexError
        except Exception as e:
            print(f'{e}')
            continue
        else:
            break


if __name__ == '__main__':
    main()
