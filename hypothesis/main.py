
from title import KattisTitleCost
import sys

class Solution(KattisTitleCost):
    
    def __init__(self)->None:
        """
        Initializer function for empty list of strings

        :return: None
        """
        self._dataList:list[str]=[]


    def get_dataList(self):
        """
        Getter for dataList

        :return:
            list[str]
        """
        return self._dataList
    
    def set_dataList(self,MTitle:str, cost_max:str) -> None:
        """
        Setter for dataList

        :return: 
            None
        """
        self._dataList=[MTitle,cost_max]

    def read_user(self)->None:
        """
        Reading user input, and splitting into two variales via whitespace
        Uses stdin input() and split()

        :return: 
            None
        """
        self._dataList = input().split()

    def solve(self):
        """
        Takes data and passes it to KTC class, solving for the output.

        :return:
            Integer
        """
        a = KattisTitleCost(self._dataList[0],float(self._dataList[1]))
        return a.costCalc()
    
    def print_ans(self) -> None:
        """
        Print function out to console

        :return:
        """
        print(self.solve())

    @staticmethod
    def main() -> None:
        """
        Main function, kicks off the rest of the code!

        :return:
            None
        """
        b = Solution()
        b.read_user()
        b.print_ans()

if __name__=="__main__":
    Solution.main()
