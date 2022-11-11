import unittest


def resultat(s, d):
    data = []
    n = len(s)
    for i in range(n):
        data.append((s[i], s[i] + d[i]))
    data.sort(key=lambda x: x[1])
    # print(data, file=sys.stderr)
    r = 1
    c = 1
    m = data[0][1]
    while c < n:
        while data[c][0] < m and c < n - 1:
            c += 1
        if data[c][0] >= m:
            m = data[c][1]
            r += 1
        c += 1
    return r


class ClasseTest(unittest.TestCase):
    def test1(self):
        s, d = [3, 9, 24, 16, 11, 28], [5, 2, 5, 9, 6, 4]
        self.assertEqual(resultat(s, d), 4)

    def test2(self):
        s, d = [2, 9, 15, 9], [5, 7, 6, 3]
        self.assertEqual(resultat(s, d), 3)

    def test3(self):
        s, d = [1, 6, 8, 4, 5, 2, 11, 24, 51, 12, 31, 27, 17], \
               [2, 3, 6, 5, 2, 4, 7, 8, 2, 3, 5, 4, 7]
        self.assertEqual(resultat(s, d), 7)


if __name__ == '__main__':
    unittest.main()
