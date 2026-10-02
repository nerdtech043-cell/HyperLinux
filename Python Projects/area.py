from math import pi
import sys

while True: 
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Exit")
    choice = int(input("\nEnter your choice: "))


    if choice == 1:
        # Area of a circle 
        radius = float(input("Enter the radius of the circle: "))
        circle_area = pi * radius ** 2 
        print(f"Area is: {circle_area:.3f}\n") 

    elif choice == 2:
        # Area of a Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        triangle_area = 0.5 * base * height 
        print(f"Area is: {triangle_area:.3f}\n")
    
    elif choice == 3:
        # Area of a Rectangle
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        rectangle_area = width * height 
        print(f"Area is: {rectangle_area:.3f}\n")

    elif choice == 4:
        sys.exit("\nGood Bye!")

    else:
        print("Invalid choice. Please try again.")
        continue 

