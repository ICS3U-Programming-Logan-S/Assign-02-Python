#!/usr/bin/env python3
# Created by: Logan Sweeney
# Created on: Dec. 2, 2021
# Area of a Trapezoid
# This program will ask the user for the dimensions of a trapezoid.
# It will then calculate the area and perimeter then display it to the user.
import math
import time
import sys


def main():

    # Melody helped me to import color. [SHE DID NOT TYPE IT, ONLY TAUGHT]
    print("\033[1;35;38mHello! Today, we will calculate the area "
          + "and perimeter of a Trapezoid.")
    side_a = int(input("\033[1;34;38mEnter side a (cm): "))
    side_b = int(input("Enter side b (cm): "))
    side_c = int(input("Enter side c (cm): "))
    side_d = int(input("Enter side d (cm): "))
    side_h = int(input("Enter side h (cm): "))
    area = (side_a + side_b) / 2 * side_h
    perimeter = (side_a + side_b + side_c + side_d)

    print("")

    # I used a reference to attempt to change the text in one line, but I
    # couldn't quite get it to work:
    # https://stackoverflow.com/questions/5426546/in-python-how-to-change-text-after-its-printed

    print('\033[1;33;38mCalculating...'),
    sys.stdout.flush()
    time.sleep(0.75)
    ...
    print('\rCalculating.. '),
    sys.stdout.flush()
    time.sleep(0.75)
    ...
    print('\rCalculating. '),
    sys.stdout.flush()
    time.sleep(1)

    print("\033[1;32;38m")
    print("The area of the trapezoid = {:.2f} cm^2. ".format(area))
    print("The perimeter of the trapezoid = {:.2f} cm. ".format(perimeter))


if __name__ == "__main__":
    main()
