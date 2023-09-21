import random

pole_list1 = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6),(1,2),(2,2),(2,3),(2,4),(2,5),(2,6),(3,1),(3,2),(3,3),(3,4),
              (3,5),(3,6),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(5,1),(5,2),(5,3)
    ,(5,4),(5,5),(5,6),(5,1),(6,2),(6,3),(6,4),(6,5),(6,6)]
class MyError(Exception):
    pass


class OutBoard(MyError):
    pass


class ErrorDot(MyError):
    pass


class ErrorShip(MyError):
    pass


class Dot():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __int__(self, length, x, y, direct):
        self.length = length
        self.st_ship = Dot(x, y)
        self.direct = direct

    def get_dots(self):
        dotship = []
        if self.direct == 'g':
            for i in range(self.length):
                dotship1 = []
                x = self.st_ship.x - 1
                y = self.st_ship.y + i - 1
                dotship1.append(x)
                dotship1.append(y)
                dotship.append(tuple(dotship1))
        elif self.direct == 'v':
            for i in range(self.length):
                dotship1 = []
                x = self.st_ship.x + i - 1
                y = self.st_ship.y - 1
                dotship1.append(x)
                dotship1.append(y)
                dotship.append(tuple(dotship1))
        return dotship

class Board:
    def __init__(self):
        self.pole = [["О" for i in range(6)] for i in range(6)]
        self.radar = [["О" for i in range(6)] for i in range(6)]
        self.dark_pole = [["О" for i in range(6)] for i in range(6)]
        self.ship = Ship()
        self.ship_list = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
        self.ship_length = [3, 2, 2, 1, 1, 1, 1]
        self.hid = False


    def add_ship(self, name_ship):
        self.name = name_ship
        for x, y in self.name.get_dots():
            self.pole[x][y] = '■'


    def countor(self, name, direct):
        self.name = name
        self.direct = direct
        for x, y, in self.name.get_dots():
            self.radar[x][y] = '1'
            if direct == 'g':
                try:
                    if (y - 1) >= 0:
                        self.radar[x][y - 1] = '1'
                    if (y + 1) <= 5:
                        self.radar[x][y + 1] = '1'
                    if (x + 1) <= 5:
                        self.radar[x + 1][y] = '1'
                    if (x - 1) >= 0:
                        self.radar[x - 1][y] = '1'
                except IndexError:
                    if (x + 1) <= 5:
                        self.radar[x + 1][y] = '1'
                    if (x - 1) >= 0:
                        self.radar[x - 1][y] = '1'
            if direct == 'v':
                try:
                    if (x - 1) >= 0:
                        self.radar[x - 1][y] = '1'
                    if (x + 1) <= 5:
                        self.radar[x + 1][y] = '1'
                    if (y + 1) <= 5:
                        self.radar[x][y + 1] = '1'
                    if (y - 1) >= 0:
                        self.radar[x][y - 1] = '1'
                except IndexError:
                    if (y + 1) <= 5:
                        self.radar[x][y + 1] = '1'
                    if (y - 1) >= 0:
                        self.radar[x][y - 1] = '1'
        return self.radar

    def proverka_na_countor(self, name):
        self.name = name
        ls = []
        for x, y in self.name.get_dots():
            if self.radar[x][y] == '1':
                ls.append(True)
            else:
                ls.append(False)
        if True in ls:
            return False



    def get_board(self, hid):
        self.hid = hid
        if hid:
            print(f'   1    2    3    4    5    6')
            c = 1
            for i in self.pole:
                print(f'{c}{i}')
                c = c + 1
        else:
            print(f'   1    2    3    4    5    6')
            c = 1
            for i in self.dark_pole:
                print(f'{c}{i}')
                c = c + 1

    def shot(self, x, y):
        if self.pole[x][y] == '■':
            self.pole[x][y] = 'X'
            self.dark_pole[x][y] = 'X'
        elif self.pole[x][y] == 'О':
            self.pole[x][y] = 'T'
            self.dark_pole[x][y] = 'T'

class Player:
    def __init__(self):
        self.user_board = Board()
        self.enemy_board = self.user_board.dark_pole

    def ask(self):
      pass

    def move(self, name):
        self.name = name
        dots = self.ask()
        x = int(dots[0])
        y = int(dots[1])
        c = 2
        b = 1
        if 0 <= x < 7 and 0 <= y < 7:
            if self.name.pole[x][y] == '■':
                self.name.shot(x, y)
                return b
            elif self.name.pole[x][y] == 'О':
                self.name.shot(x, y)
                b = 3
                return b
            elif self.name.pole[x][y] == 'X':
                self.name.shot(x, y)
                b = 4
                return b
            elif self.name.pole[x][y] == 'T':
                self.name.shot(x, y)
                b = 4
                return b


class User(Player):
    def ask(self):
        valid = True
        while valid:
            print('ход игрока')
            try:
                tochkax, tochkay = input('введите х:'), input('введите y:')
                b = [int(tochkax) - 1, int(tochkay) - 1]
            except ValueError:
                print('введите число')
                continue
            if 0 < int(tochkax) < 7 and 0 < int(tochkax) < 7:
                valid = False
                break
            print('введите корректное значение от 1 до 6')
        return b

    def get_board(self, param):
        pass


class AI(Player):
    def ask(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        b = [x - 1, y - 1]
        return b

class Game():
    def __init__(self):
        self.user = User()
        self.board_user = Board()
        self.enemy = AI()
        self.board_enemy = Board()


    def random_board(self, name):
        count = 0
        c = 2000
        out = "xxx"
        b = 0
        for i in name.ship_list:
            while c >= 0:
                try:
                    i = Ship()
                    i.direct = random.choice('vg')
                    i.st_ship = Dot(random.randint(1, 6), random.randint(1, 6))
                    i.length = name.ship_length[count]
                    if i.get_dots()[i.length - 1] in pole_list1 and name.proverka_na_countor(i) is not False:
                        name.add_ship(i)
                        name.countor(i, i.direct)
                        b = b + 1
                        break
                    c = c - 1
                    if c == 0:
                        return c

                except IndexError:
                    continue
            count = count + 1
        if b == 7:
            return out

    def greet(self):
        print('игра в крестики нолики против компа')
        print('вводим значение от 1 до 6 по ветикали - х')
        print('потом значение от 1 до 6 по горизонтали - y')
        print('начало игры')

    def loop(self):
        while True:
            b = self.random_board(self.board_user)
            if b == 0:
                self.board_user.pole = [["О" for i in range(6)] for i in range(6)]
                self.board_user.radar = [["О" for i in range(6)] for i in range(6)]
            elif b == "xxx":
                break
        while True:
            b = self.random_board(self.board_enemy)
            if b == 0:
                self.board_enemy.pole = [["О" for i in range(6)] for i in range(6)]
                self.board_enemy.radar = [["О" for i in range(6)] for i in range(6)]
            elif b == "xxx":
                break
        ai_lives = 11
        user_lives = 11
        while True:
            while True:
                if ai_lives == 0:
                    break
                print('доска игрока')
                self.board_user.get_board(True)
                print('доска противника')
                self.board_enemy.get_board(False)
                b = self.user.move(self.board_enemy)
                if b == 3:
                    print('мимо')
                    break
                elif b == 4:
                    print('в эту точку уже стреляли')
                    continue
                ai_lives = ai_lives - 1
                print('жизни компа', ai_lives)
            if ai_lives == 0:
                print('игрок победил')
                break
            while True:
                if user_lives == 0:
                    break
                print('ход компьютера')
                e = self.enemy.move(self.board_user)
                if e == 3:
                    print('комп промазал')
                    break
                elif e == 4:
                    continue
                user_lives = user_lives - 1
            if user_lives == 0:
                print('компьютер победил')
                break
        print('игра закончена')

    def start(self):
        self.greet()
        self.loop()





s = Game()
s.start()

