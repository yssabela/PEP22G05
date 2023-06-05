def is_a_triangle(x, y, z):
    if x + y <= z or y + z <= x or x + z <= y:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# or more compact

def is_a_triangle(x, y, z):
    return x + y > z and y + z > x and z + x > y


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# install the function in a larger program. ask the user for 3 values and make use of the function

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# triangle and the Pythagorean theorem:

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(1, 3, 4))
print(is_a_right_triangle(1, 3, 4))


# relationship between hypotenuse and the remaining sides :

def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle')
else:
    print('No, it can not be a triangle')
