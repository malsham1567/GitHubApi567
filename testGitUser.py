import unittest

from GetHub_user import get_reps


class testGitUser(unittest.TestCase):
    def testGetRepos(self):
        self.assertEqual(get_reps('m6ni'), ['Repo: homework9- Number of commits: 2', 'Repo: home_work9 Number of commits: 7', 'Repo: homwork9_1 Number of commits: 2'])
        self.assertEqual(get_reps('talal3456'), 'Invalid user')
        self.assertEqual(get_reps(','), 'Invalid user')


if __name__ == '__main__':
    unittest.main()
