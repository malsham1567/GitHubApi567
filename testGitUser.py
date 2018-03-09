import unittest
from unittest import mock
from GetHub_user import get_reps


class TestGetReps(unittest.TestCase):
    @mock.patch('GetHub_user.get_info')
    def testGetRepos(self,mockedReq):
        mockedReq.return_value = ['Repo: homework9- has  0 commits', 'Repo: home_work9 has  7 commits', 'Repo: homwork9_1 has  2 commits']
        self.assertEqual(get_reps('m6ni'), ['Repo: homework9- has  0 commits', 'Repo: home_work9 has  7 commits', 'Repo: homwork9_1 has  2 commits'])
        mockedReq.return_value = 'Invalid user'
        self.assertEqual(get_reps('talal3456'), 'Invalid user')
        mockedReq.return_value = 'Invalid user'
        self.assertEqual(get_reps(','), 'Invalid user')


if __name__ == '__main__':
    unittest.main()
