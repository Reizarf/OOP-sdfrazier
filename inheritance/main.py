import sys
from number_list import *

class Solution(object):
    """
    Solution Class to kick off calculations, input, and output.
    """
    def __init__(self)->None:
        self._usrDataList:'list[str]'=[]#empty list of strings

    def get_UserIn(self)->'list[str]':
        """
        Function to get userInput

        :return:list[str]
        """
        return self._usrDataList
    
    def set_UserIn(self,usrDataList:'list[str]')->None:
        """
        Function to set data in list of strings

        :return:None
        """
        self._usrDataList=usrDataList

    def read_UserIn(self)->None:
        """
        Uses sys.stdin to read user input, puts it into usrDataList variable.

        :return:None
        """
        self._usrDataList= sys.stdin.readlines()
        #self._usrDataList=input()
    
    def solve(self,container:'list[str]')->'PrintStatistics':
        """
        Actually solve the kattis problem using functions in
        number_list.py

        :return:PrintStatistics object
        """
        ans = PrintStatistics(container)
        return ans
    
    def out_Answer(self)->None:
        """
        Print Function

        :return:None
        """
        
        counter:int = 1
        for i in self._usrDataList:
            statOut = self.solve(i.split())
            print("Case " + str(counter) + ":",statOut)
            counter+=1
    
    @staticmethod
    def main() -> None:
        
        a = Solution()
        a.read_UserIn()
        a.out_Answer()

        # PrintStatistics.statFormat()

if __name__ == "__main__":
    Solution.main()