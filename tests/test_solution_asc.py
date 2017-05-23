from unittest import TestCase


class TestSolution_asc(TestCase):
    def test_solution_asc(self):
        from build import solution_asc
        d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        result = solution_asc(d)
        self.assertEqual(result, [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)])

    def test_solution_desc(self):
        from build import solution_desc
        d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        result = solution_desc(d)
        self.assertEqual(result, [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)])
