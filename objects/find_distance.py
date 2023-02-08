import math
#mypy

class Point:
    """
    Docstring things
    
    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initializes the position of a new point.
        X and Y coordinates are specified, else origin
        """
        self.move(x,y)
    
    def move(self, x: float, y: float)-> None:
        """
        Move the point to a new location via X and Y axis.
        """
        self.x = x
        self.y = y
     
    def reset(self) -> None:
        """
        Reset the point back to origin
        """
        self.move(0,0)

    def find_distance(self, other:"Point") -> float:
        """
        Calculate the Euclidean distance from this point and another
        passsed as a parameter.
        """
        return math.hypot(self.x - other.x,self.y - other.y)
    
def main() -> None:
    """
    Does the actual work!
    """
    p1 = Point()
    p2 = Point(5,6)
    print(f"{p1.find_distance(p2)=}")

if __name__ == "__main__":
    main()
