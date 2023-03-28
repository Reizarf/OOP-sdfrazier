from main import Solution
from io import StringIO
from unittest.mock import *
import unittest

class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.sul_main:'Solution'=Solution()
        self.sul_main.set_dataList('test','4')
    
    @patch('sys.stdout',new_callable=StringIO)
    def test_solution(self,mock_stdout:StringIO)->None:
        self.sul_main.print_ans()
        self.assertEqual(mock_stdout.getvalue(),'4\n')

    @patch('sys.stdin')
    def test_user_data(self,mock_stdin) -> None:
        mock_stdin.read.return_value = 'greetings 99.99'
        self.sul_main.read_user()
        self.assertEqual(self.sul_main.get_dataList(),['greetings','99.99'])

    @patch('sys.stdin')
    def test_main(self,mock_stdin) -> None:
        a = 'wowza 2.39'
        a.split()
        mock_stdin.read.return_value = a
        self.sul_main.main()

if __name__ == '__main__':
    unittest.main(verbosity=2)