from polygonarea import KattisPolygon


class Solution(KattisPolygon):
    """
    Solution Convex Polygon Area Class
    """
    
    def run(self)->int:
        """
        Call read and print area function in polygonarea file
        """
        n = KattisPolygon.read_and_print_area()
        return n

    def getSelf(self)->int:
        """
        Default getter
        """
        return self
    
    def setSelf(self)->int:
        """
        Default setter
        """
        self = 0
        return self


if __name__ == "__main__":
    solution = Solution()
    solution.run()