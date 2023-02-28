import math
from typing import List

class KattisPolygon():
    # Function to calculate the area of a convex polygon
    def calculate_polygon_area(points) -> int:
        """
        Calculates area based on points map variable

        Args:
            points(int)
        
        Solves shoelace mathematics

        Return -> int
        """
        n = len(points)
        
        area = 0

    #solve for area using shoelace formula
        for i in range(n):
            j = (i + 1) % n
            area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
        area = abs(area) / 2
        return area
    
    def read_and_print_area() -> None:
        """
        Takes user input and converts to integers

        Return -> None.
        """
        # Get integer input from the user
        n = int(input())

        # Loop through each polygon and calculate its area
        for i in range(n):
            polygon_input = input().split()
            m = int(polygon_input[0])
            points = []
            for j in range(m):
                x, y = map(int, [polygon_input[j*2+1], polygon_input[j*2+2]])
                points.append((x, y))

            area = KattisPolygon.calculate_polygon_area(points)
            print(area)
    
# if __name__ == "__main__":
#     KattisPolygon.read_and_print_area()
