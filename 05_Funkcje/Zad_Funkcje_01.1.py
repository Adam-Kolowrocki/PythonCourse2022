# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def circle_area(radius):
    """This function returns circle area from radius given as parameter"""
    print('Area of circle with radius', radius, 'is =', 3.141592 * (radius * radius))
    return


circle_area(radius = int(input('Give circle radius to calculate area -> ')))
