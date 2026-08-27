import math

def CircleArea():
    r = float(input("enter the radius of circle: "))
    area = math.pi*pow(r, 2)
    print("The area of this circle is: ", area)

CircleArea()