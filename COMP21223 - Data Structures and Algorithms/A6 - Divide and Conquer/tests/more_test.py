import unittest

from invasion import AlienInvasion

class MoreTest(unittest.TestCase):
    def test_count_markers(self):
        V = AlienInvasion()

        a = [-2, -1, 0, 1]
        c = 2

        res = V.count_markers(a, c)
        assert res == 4

    def test_count_markers_2(self):
        V = AlienInvasion()

        A = [x for x in range(-20, 300, 3)]

        c = 35

        res = V.count_markers(A, c)
        self.assertEqual(28, res, "expected {} got {}".format(28, res))
        #assert res == 28

    def test_break_control(self):
        V = AlienInvasion()

        A = [-90, 1, 95]
        c = 99

        res = V.break_control(A, c)
        self.assertTrue(res == 0 or res == 1 or res==2)

