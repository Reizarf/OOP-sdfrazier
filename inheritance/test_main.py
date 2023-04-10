from number_list import *
from io import StringIO
from unittest.mock import *
import unittest

class TestMain(unittest.TestCase):

    def setUp(self)->None:
        self.sul_main:'NumberList'=NumberList()
        self._sul_main.set_dataList('2','4','10')

    @patch('sys.stdout',new_callable=StringIO)
    def test_solution(self,mock_stdout:StringIO)->None:
        self.sul_main.print_ans()
        self.assertEqual(mock_stdout.getvalue(),'Case 1: 4 10 6')

    @patch('sys.stdin')
    def test_user_data(self,mock_stdin)->None:
        mock_stdin.read.return_value = '99 4 10'
        self.sul_main.read_user()
        self.assertEqual(self.sul_main.get_dataList(),['99','4','10'])

    @patch('sys.stdin')
    def test_main(self,mock_stdin)->
        a = '99 4 10'
        a.split()
        mock_stdin.read.return_value=a
        self._sul_main()

if __name__ == '__main__':
    unittest.main(verbosity=2)