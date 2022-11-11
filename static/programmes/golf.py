import unittest

class Map:
    def __init__(self, map, boolmap=None, sol=None):
        self.height = len(map)
        self.width = len(map[0])
        self.map = map
        if boolmap:
            self.boolmap = boolmap
        else:
            self.boolmap = [[True for j in range(self.width)] for i in
                            range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    if map[i][j] not in {'H', '.', 'X'}:
                        self.boolmap[i][j] = False
        if sol:
            self.sol = sol
        else:
            self.sol = [['.' for j in range(self.width)] for i in
                        range(self.height)]

    def gagne(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] not in {'H', '.', 'X'}:
                    return False
        return True

    def coupValide(self, i, j, dir):
        n = int(self.map[i][j])
        c = 0
        if dir == "v":
            while i < self.height - 1 and self.boolmap[i + 1][j] and c < n:
                c += 1
                i += 1
        elif dir == "^":
            while i > 0 and self.boolmap[i - 1][j] and c < n:
                c += 1
                i -= 1
        elif dir == "<":
            while j > 0 and self.boolmap[i][j - 1] and c < n:
                c += 1
                j -= 1
        elif dir == '>':
            while j < self.width - 1 and self.boolmap[i][j + 1] and c < n:
                c += 1
                j += 1
        else:
            print("pb !!!")
        if c == n and self.map[i][j] != 'X' and not (
                n == 1 and self.map[i][j] != 'H'):
            return True
        else:
            return False

    def balle(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] not in {'H', '.', 'X'}:
                    return i, j
        return -1, -1

    def deplacement(self, i, j, dir):
        n = int(self.map[i][j])
        self.map[i][j] = '.'
        for k in range(n):
            self.sol[i][j] = dir
            if dir == 'v':
                i += 1
            elif dir == "^":
                i -= 1
            elif dir == "<":
                j -= 1
            elif dir == ">":
                j += 1
            else:
                print("pb !!!")
            self.boolmap[i][j] = False
        if self.map[i][j] != 'H':
            self.map[i][j] = str(n - 1)
        return i, j, n

    def backTrack(self, i, j, n, dir):
        if self.map[i][j] != 'H':
            self.map[i][j] = '.'
        for k in range(n):
            self.boolmap[i][j] = True
            if dir == '<':
                j += 1
            elif dir == '>':
                j -= 1
            elif dir == 'v':
                i -= 1
            elif dir == '^':
                i += 1
            self.sol[i][j] = '.'
        self.map[i][j] = str(n)

    def solution(self):
        if self.gagne():
            return True
        i, j = self.balle()
        for dir in ['v', '^', '<', '>']:
            if self.coupValide(i, j, dir):
                new_i, new_j, n = self.deplacement(i, j, dir)
                if self.solution():
                    return True
                self.backTrack(new_i, new_j, n, dir)
        return False

    def result(self):
        if (not self.solution()):
            print("Solution does not exist")
        else:
            return self.returnSolution()

    def returnSolution(self):
        res = []
        for i in self.sol:
            p = ""
            for j in i:
                p += j
            res.append(p)
        return res


class ClasseTest(unittest.TestCase):

    def test1(self):
        map = Map([['1', 'H']])
        self.assertEqual(map.result(), ['>.'])

    def test2(self):
        map = Map([['2', '.', 'X'], ['.', '.', 'H'], ['.', 'H', '1']])
        self.assertEqual(map.result(), ['v..', 'v..', '>.^'])

    def test3(self):
        map = Map([['4', '.', '.', 'X', 'X'], ['.', 'H', '.', 'H', '.'],
                   ['.', '.', '.', 'H', '.'], ['.', '2', '.', '.', '2'],
                   ['.', '.', '.', '.', '.']])
        self.assertEqual(map.result(),
                         ['v....', 'v...<', 'v^..^', 'v^.^^', '>>>^.'])

    def test4(self):
        map = Map(
            [['3', '.', '.', 'H', '.', '2'], ['.', '2', '.', '.', 'H', '.'],
             ['.', '.', 'H', '.', '.', 'H'], ['.', 'X', '.', '2', '.', 'X'],
             ['.', '.', '.', '.', '.', '.'], ['3', '.', '.', 'H', '.', '.']])
        self.assertEqual(map.result(), ['>>>..v', '.>>>.v', '>>....', '^..v..',
                                        '^..v..', '^.....'])

    def test5(self):
        map = Map([['5', '.', '.', '.', '.', '.', 'X', '.', '.', '3', '.', '.',
                    '.', 'H', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                    '.', '.', '.', '.', '.', '.', 'H', 'X', '.', '.', '.', '.',
                    '.', '4', 'X', 'H'],
                   ['.', '.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', 'X',
                    'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.', '.',
                    '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', '2', '.',
                    '.', 'H', 'X', 'X'],
                   ['.', '.', '.', '.', '.', '.', '4', 'H', '.', '.', '.', '.',
                    '.', '.', '.', '.', 'X', '.', '.', '4', 'H', '.', 'H', '.',
                    '.', '.', '3', '.', '.', 'H', '.', '.', '.', '.', '4', '.',
                    '.', '.', '.', '.'],
                   ['.', 'H', 'H', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                    'H', '5', 'X', 'X', '.', '.', '.', '.', '.', 'H', '.', '.',
                    '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                    '.', '.', '5', '.'],
                   ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                    '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', 'X', '.', '2',
                    '4', '4', '.', '2', '.', 'X', '.', '.', 'H', '.', '5', '.',
                    '.', '.', '.', '.'],
                   ['X', '.', 'H', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                    '.', 'X', 'X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.',
                    '4', '4', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.',
                    '.', '.', '.', '5'],
                   ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                    '.', '.', 'X', 'X', '4', '.', '.', '.', '.', '.', '.', '.',
                    '3', '.', '.', '.', 'H', '.', '.', '.', '.', '.', '.', '.',
                    '.', '.', '3', '.'],
                   ['.', '.', '.', '3', '.', '.', '.', '.', '.', '.', '3', '.',
                    '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.',
                    '.', '.', '.', 'H', '.', 'H', '.', '.', '.', '.', '.', '.',
                    '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.', '.', '.', 'H', 'H', '.', '.', '.',
                    '.', '.', 'X', 'X', 'X', 'X', 'X', '.', 'H', '.', 'X', '.',
                    '.', '.', '.', '.', '.', '.', 'X', 'X', '.', '.', '.', '.',
                    'H', '.', 'X', 'X'],
                   ['3', '.', '.', '.', '.', '.', '.', '.', '.', '5', '.', '.',
                    '.', '.', 'H', '.', 'H', '.', '.', '.', '.', '.', 'X', '.',
                    '.', '.', '.', '.', '.', '.', 'H', 'X', '.', '.', '.', '.',
                    '.', '.', 'X', 'H']])
        self.assertEqual(map.result(),
                         ['>>>>>v...v..>........v<<<>>>v..<<<<<<<..',
                          '.....v...v..^........v..^^..v.....>>>..^',
                          '..v<<vv..v..^<<<<<<<.v.<^^v.>.v<<<<....^',
                          '....^vv^<<...>>>>>v.^..^^^v...v..v<<<<<^',
                          '.^<<^vv...>>^.....v.^..^^^vv..v..v>>>>>^',
                          '...^^vv...^.......v.^<<<<vvv..>>^vv<<<<<',
                          '>>^^^v>>>v^.v<<<<.v..v<<<vv>.....vvv<<<.',
                          '^..^^>>v.v^.v..v<<<..v...v>.>.v<<<vv....',
                          '^...^....<..v..v.....<...v..^.v...v>....',
                          '^...^<<<<<..>>.>.........>>>^.....>>>>>.'])


if __name__ == '__main__':
    unittest.main()