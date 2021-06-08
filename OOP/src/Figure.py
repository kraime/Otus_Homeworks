import math


class Figure:

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    def add_area(self, any_figure):
        if Figure not in any_figure.__class__.__bases__:
            raise TypeError('Hey! Ты передал не класс Figure')
        return self.area + any_figure.area

    #  Добавили декоратор, который превращает функцию в свойство класса
    @property
    def area(self):
        return 0


class Triangle(Figure):
    name = "triangle"

    def __init__(self, angles, a, b, c):
        super().__init__(self.name, angles)
        self.a = a
        self.b = b
        self.c = c

    # Переопределили свойство area для подсчета площади Треугольника
    @property
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    # Подсчет периметра Треугольника
    def get_triangle_perimeter(self):
        return self.a + self.b + self.c


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, angles, a, b):
        super().__init__(self.name, angles)
        self.a = a
        self.b = b

    # Переопределили свойство area для подсчета площади Прямоугольника
    @property
    def area(self):
        return self.a * self.b

    # Подсчет периметра Прямоугольника
    def get_rectangle_perimeter(self):
        return 2 * self.a + 2 * self.b


class Square(Figure):
    name = "square"

    def __init__(self, angles, a):
        super().__init__(self.name, angles)
        self.a = a

    # Переопределили свойство area для подсчета площади Квадрата
    @property
    def area(self):
        return self.a ** 2

    # Подсчет периметра Квадрата
    def get_square_perimeter(self):
        return 4 * self.a


class Circle(Figure):
    name = "circle"

    def __init__(self, angles, r):
        super().__init__(self.name, angles)
        self.r = r

    # Переопределили свойство area для подсчета площади Круга
    @property
    def area(self):
        return math.pi * self.r ** 2

    # Подсчет периметра Круга
    def get_circle_perimeter(self):
        return 2 * math.pi * self.r


angles = None

triangle = Triangle(angles, 10, 8, 7)
print("Triangle Area : {}".format(triangle.area))
print("Triangle Perimeter : {}".format(triangle.get_triangle_perimeter()))

rectangle = Rectangle(angles, 5, 8)
print("Rectangle Area : {}".format(rectangle.area))
print("Rectangle Perimeter : {}".format(rectangle.get_rectangle_perimeter()))

square = Square(angles, 7)
print("Square Area : {}".format(square.area))
print("Square Perimeter : {}".format(square.get_square_perimeter()))

circle = Circle(angles, 15)
print("Circle Area : {}".format(circle.area))
print("Circle Perimeter : {}".format(circle.get_circle_perimeter()))

# print("Сумма площади треугольника и сумма площади прямоугольника : {}".format(triangle.add_area(rectangle)))
# Проверка на ошибку фигура ли это или нет
# print(triangle.add_area(4532))
