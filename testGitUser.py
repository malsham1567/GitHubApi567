import unittest

from GetHub_user import get_reps


class TestGetReps(unittest.TestCase):
    def testGetRepos(self):
        self.assertEqual(get_reps('m6ni'), ['Repo: homework9- has  0 commits', 'Repo: home_work9 has  7 commits', 'Repo: homwork9_1 has  2 commits'])
        self.assertEqual(get_reps('talal3456'), 'Invalid user')
        self.assertEqual(get_reps(','), 'Invalid user')


if __name__ == '__main__':
    unittest.main()
