from sys import stdin
case = 1

for line in stdin:
    numbers = [int(x) for x in line.split()]
    numbers = numbers[1:]
    biggest = max(numbers)
    smallest = min(numbers)
    difference = biggest - smallest
    print("Case " + str(case) + ": " + str(smallest) + " " + str(biggest) + " " + str(difference))
    case += 1
