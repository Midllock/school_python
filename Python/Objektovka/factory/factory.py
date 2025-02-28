class Shape:
    def render(self):
        print("Initialize to render some shape...")

class Square(Shape):
    def render(self):
        super().render()
        print("Rendering square...")

class Triagle(Shape):
    def render(self):
        super().render()
        print("Rendering triagle...")

class Circle(Shape):
    def render(self):
        super().render()
        print("Rendering circle...")

class Rectangle(Shape):
    def render(self):
        super().render()
        print("Rendering rectangle...")

class Factory:
    __article = ["Sqeuare", "Triagle", "Circle", "Rectangle"]
    @staticmethod
    def create_shape(representative):
        if representative in Factory.__article:
            return globals()[representative]()
        else:
            return Square()
    """
    match representative:
        case "Sqeuare":
            return Square()

        case "Triagle":
            return Triagle()

        case "Circle":
            return Circle()

        case _:
            return Square()
    """ 

my_square = Factory.create_shape("Square")
my_square.render()

my_square = Factory.create_shape("Triangle")
my_square.render()

my_square = Factory.create_shape("Circle")
my_square.render()

my_square = Factory.create_shape("Rectangle")
my_square.render()