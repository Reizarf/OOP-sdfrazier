from hello import HelloWorld
"""
Manager
Class
"""

class Main(object):
    """
    Main Class
    """
    def __init__(self)->None:
        self._solution: 'HelloWorld' = HelloWorld


    def solve(self)->None:
        self._solution.print_message()
    
    @staticmethod
    def main() -> None:
        obj = Main()
        obj.solve()



if __name__ == '__main__':
    Main.main()
