#!/usr/bin/pyhthon3
import math

def calculate_circle_area(radius):
    """
    Given a radius, this function calculates and returns the area of a circle.
    """
    return math.pi * (radius ** 2)

def main():
    r = float(input("Enter the radius of the circle: "))
    print("Area of the circle is: {:.2f}".format(calculate_circle_area(r)))

if __name__ == "__main__":
    main()
    