import unittest
from task2.src.task2 import solve


class TestSolve(unittest.TestCase):
    def test_solve_valid_case(self):
        result = solve(3, 1)
        expected = [
            '1 3 2',
            '2 1 3',
            '3 2 1'
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_solve_valid_case_2(self):
        result = solve(5, 3)
        expected = [
            '1 2 3 5 4',
            '1 2 4 3 5',
            '1 2 5 4 3',
            '1 3 2 4 5',
            '1 4 3 2 5',
            '1 5 3 4 2',
            '2 1 3 4 5',
            '3 2 1 4 5',
            '4 2 3 1 5',
            '5 2 3 4 1'
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_solve_no_fixed_elements(self):
        result = solve(3, 0)
        expected = [
            '2 3 1',
            '3 1 2'
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_solve_all_fixed_elements(self):
        result = solve(3, 3)
        expected = [
            '1 2 3'
        ]
        self.assertEqual(result, expected)

    def test_solve_large_case(self):
        result = solve(4, 2)
        self.assertIn('1 2 4 3', result)
        self.assertIn('1 3 2 4', result)



if __name__ == '__main__':
    unittest.main()
