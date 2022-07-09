from abc import ABC


class Shape(ABC):

    def draw(self):
        return None


class Rectangle(Shape):

    def draw(self) -> str:
        return f"Shape: Rectangle"


class Circle(Shape):

    def draw(self) -> str:
        return f"Shape: Circle"


class ShapeDecorator(Shape):
    _decorated_shape = None

    def __init__(self, decorated_shape: Shape):
        self._decorated_shape = decorated_shape

    def draw(self):
        self._decorated_shape.draw()


class RedShapeDecorator(ShapeDecorator):

    def __init__(self, decorated_shape: Shape):
        super().__init__(decorated_shape)

    def draw(self):
        return self.__set_red_border()

    def __set_red_border(self) -> str:
        return f'Border color: Red    {self._decorated_shape.draw()}'


if __name__ == '__main__':
    circle = Circle()
    red_rectangle = RedShapeDecorator(Rectangle())
    red_circle = RedShapeDecorator(circle)

    print(circle.draw())
    print(red_rectangle.draw())
    print(red_circle.draw())
