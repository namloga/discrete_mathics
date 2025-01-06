import unittest
from task1.src.task1 import task1


class TestRelationProperties(unittest.TestCase):
    def test_reflexive(self):
        S = [1, 2, 3]
        R = [(1, 1), (2, 2), (3, 3)]
        properties = task1(S, R)
        self.assertTrue(properties['Reflexive'])
        self.assertFalse(properties['Anti-reflexive'])
        self.assertFalse(properties['Not-reflexive'])


    def test_anti_reflexive(self):

        S = [1, 2, 3]
        R = [(1, 2), (2, 3)]
        properties = task1(S, R)
        self.assertTrue(properties['Anti-reflexive'])
        self.assertFalse(properties['Reflexive'])
        self.assertFalse(properties['Not-reflexive'])

    def test_not_reflexive(self):
        S = [1, 2, 3]
        R = [(1, 1), (2, 3)]
        properties = task1(S, R)
        self.assertTrue(properties['Not-reflexive'])
        self.assertFalse(properties['Reflexive'])
        self.assertFalse(properties['Anti-reflexive'])


    def test_symmetric(self):
        S = [1, 2]
        R = [(1, 2), (2, 1)]
        properties = task1(S, R)
        self.assertTrue(properties['Symmetric'])
        self.assertFalse(properties['Asymmetric'])
        self.assertFalse(properties['Not-symmetric'])


    def test_asymmetric(self):
        S = [1, 2]
        R = [(1, 2)]
        properties = task1(S, R)
        self.assertTrue(properties['Asymmetric'])
        self.assertFalse(properties['Symmetric'])
        self.assertFalse(properties['Not-symmetric'])


    def test__anti_symmetric(self):
        S = [1, 2, 3]
        R = [(1, 1), (2, 2), (3, 3), (1, 2)]
        properties = task1(S, R)
        self.assertTrue(properties['Anti-symmetric'])
        self.assertFalse(properties['Symmetric'])

    def test_not_symmetric(self):
        S = [1, 2, 3]
        R = [(1, 2), (2, 1), (2, 3)]
        properties = task1(S, R)
        self.assertTrue(properties['Not-symmetric'])
        self.assertFalse(properties['Symmetric'])
        self.assertFalse(properties['Asymmetric'])

    def test_transitive(self):
        S = [1, 2, 3]
        R = [(1, 2), (2, 3), (1, 3)]
        properties = task1(S, R)
        self.assertTrue(properties['Transitive'])
        self.assertFalse(properties['Not-transitive'])

    def test_anti_transitive(self):
        S = [1, 2, 3]
        R = [(1, 2), (2, 3)]
        properties = task1(S, R)
        self.assertTrue(properties['Anti-transitive'])
        self.assertFalse(properties['Transitive'])
        self.assertFalse(properties['Not-transitive'])

    def test_not_transitive(self):
        S = [1, 2, 3]
        R = [(1, 2),(2, 3),(1, 3),(3, 1)]
        properties = task1(S, R)
        self.assertFalse(properties['Transitive'])
        self.assertFalse(properties['Anti-transitive'])
        self.assertTrue(properties['Not-transitive'])

    def test_large_reflexive(self):
        """Kiểm tra quan hệ phản xạ với dữ liệu lớn."""
        S = list(range(1, 21))  # 20 phần tử
        R = [(i, i) for i in S]  # Tất cả các phần tử đều có quan hệ với chính nó
        properties = task1(S, R)
        self.assertTrue(properties['Reflexive'])
        self.assertFalse(properties['Anti-reflexive'])
        self.assertFalse(properties['Not-reflexive'])

    def test_large_anti_reflexive(self):
        S = list(range(1, 21))
        R = [(i, i + 1) for i in range(1, 20)]
        properties = task1(S, R)
        self.assertTrue(properties['Anti-reflexive'])
        self.assertFalse(properties['Reflexive'])
        self.assertFalse(properties['Not-reflexive'])

    def test_large_symmetric(self):
        S = list(range(1, 11))
        R = [
            (1, 2), (2, 1),
            (3, 4), (4, 3),
            (5, 6), (6, 5),
            (7, 8), (8, 7),
            (9, 10), (10, 9)
        ]
        properties = task1(S, R)
        self.assertTrue(properties['Symmetric'])
        self.assertFalse(properties['Asymmetric'])
        self.assertFalse(properties['Not-symmetric'])

    def test_large_asymmetric(self):
        S = list(range(1, 11))
        R = [
            (1, 2),
            (3, 4),
            (5, 6),
            (7, 8),
            (9, 10)
        ]
        properties = task1(S, R)
        self.assertTrue(properties['Asymmetric'])
        self.assertFalse(properties['Symmetric'])
        self.assertFalse(properties['Not-symmetric'])

    def test_large_anti_symmetric(self):
        S = list(range(1, 11))
        R = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
            (6, 7), (7, 8), (8, 9), (9, 10)
        ]
        properties = task1(S, R)
        self.assertTrue(properties['Anti-symmetric'])
        self.assertFalse(properties['Symmetric'])
        self.assertFalse(properties['Not-symmetric'])

    def test_large_not_symmetric(self):
        S = list(range(1, 11))
        R = [
            (1, 2), (2, 1),
            (3, 4),
            (5, 6), (6, 5),
            (7, 8),
            (9, 10), (10, 9)
        ]
        properties = task1(S, R)
        self.assertTrue(properties['Not-symmetric'])
        self.assertFalse(properties['Symmetric'])
        self.assertFalse(properties['Asymmetric'])

    def test_large_transitive(self):
        S = list(range(1, 11))
        R = [
            (1, 2), (2, 3), (1, 3),
            (4, 5), (5, 6), (4, 6),
            (7, 8), (8, 9), (7, 9)
        ]
        properties = task1(S, R)
        self.assertTrue(properties['Transitive'])
        self.assertFalse(properties['Not-transitive'])

    def test_large_anti_transitive(self):
        S = list(range(1, 11))
        R = [
            (1, 2), (2, 3)
        ]
        properties = task1(S, R)
        self.assertTrue(properties['Anti-transitive'])
        self.assertFalse(properties['Transitive'])
        self.assertFalse(properties['Not-transitive'])

    def test_not_transitive_large(self):
        S = [1, 2, 3, 4, 5, 6, 7]
        R = [
            (1, 2), (2, 3), (3, 4), (4, 5), (1, 5),
            (2, 4), (3, 1), (5, 6), (6, 7), (7, 5)
        ]
        properties = task1(S, R)

        self.assertFalse(properties['Transitive'])
        self.assertFalse(properties['Anti-transitive'])
        self.assertTrue(properties['Not-transitive'])
if __name__ == '__main__':
    unittest.main()
