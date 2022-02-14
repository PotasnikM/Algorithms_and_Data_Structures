import area_and_perimeter as a_p


if __name__ == '__main__':
    # Checking if input values create a triangle
    a, b, c = input('Enter the edges lengths of triangle: ').split()
    a = float(a)
    b = float(b)
    c = float(c)
    if a + b <= c or a + c <= b or b + c <= a:
        print('Previous input doesn\'t make a triangle')
        a, b, c = input('Enter the correct edges lengths of triangle: ').split()
    # Creating object my_triangle of Triangle class
    my_triangle = a_p.Triangle(a, b, c)
    # Printing area and perimeter of my_triangle
    print('Area of triangle is {} and perimeter is {}.'.format(my_triangle.area(), my_triangle.perimeter()))
    # Getting the radius of circle
    r = input('Enter the radius length of circle: ')
    # Creating my_circle object of Circle class
    my_circle = a_p.Circle(r)
    # Printing area and perimeter of my_circle
    print('Area of circle is {} and perimeter is {}.'.format(my_circle.area(), my_circle.perimeter()))
    # Getting the edge length of square
    x = input('Enter the edge length of square: ')
    # Creating my_square object of Square class
    my_square = a_p.Square(x)
    # Printing area and perimeter of my_square
    print('Area od square is {} and perimeter is {}.'.format(my_square.area(), my_square.perimeter()))
