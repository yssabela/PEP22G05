def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))


def lb_to_kg(lb):
    return lb * 0.45

print(lb_to_kg(1))


def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6, 0))


# what is the BMI of a person 5'7'' tall and weighing 176 lbs??

def ft_and_inch_to_m(ft,inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight/height**2

print(bmi(weight=lb_to_kg(176),height=ft_and_inch_to_m(5,7)))

