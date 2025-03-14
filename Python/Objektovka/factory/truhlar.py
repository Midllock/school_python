class Furniture:
    def __init__(self, **kwargs):
        if not all(key in kwargs for key in ["material", "width", "height", "depth"]):
            raise ValueError("Chybí povinné parametry")
        self.__material = kwargs["material"]
        self.__width = kwargs["width"]
        self.__height = kwargs["height"]
        self.__depth = kwargs["depth"]
        self.__amount = kwargs.get("amount", 1)
    def __str__(self):
        return f"Material: {self.__material}, Width: {self.__width}, Height: {self.__height}, Depth: {self.__depth}, Amount: {self.__amount}"
class Table(Furniture):
    def __str__(self):
        return f"Table: {super().__str__()}"
class Chair(Furniture):
    def __str__(self):
        return f"Chair: {super().__str__()}"
class ChestOfDrawers(Furniture):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "drawers" not in kwargs:
            raise ValueError("Chybí počet zásuvek")
        self.__num_of_drawers = kwargs["drawers"]
    def __str__(self):
        return f"Chest of Drawers: {super().__str__()}, Number of Drawers: {self.__num_of_drawers}"
class ShelfCabinet(Furniture):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "shelves" not in kwargs:
            raise ValueError("Chybí počet polic")
        self.__num_of_shelves = kwargs["shelves"]
    def __str__(self):
        return f"Shelf Cabinet: {super().__str__()}, Number of Shelves: {self.__num_of_shelves}"
class Factory:
    def __init__(self):
        self.__furniture = {
            "table": Table,
            "chair": Chair,
            "chest of drawers": ChestOfDrawers,
            "shelf cabinet": ShelfCabinet
        }
    def make(self, **kwargs):
        if "furniture" not in kwargs:
            raise ValueError("Chybí typ nábytku")
        furniture_type = kwargs.pop("furniture")
        if furniture_type not in self.__furniture:
            raise ValueError("Neplatný typ nábytku")
        return self.__furniture[furniture_type](**kwargs)
f = Factory()
chest_of_drawers = f.make(
    furniture="chest of drawers",
    material="oak",
    width=90,
    height=180,
    depth=60,
    amount=4,
    drawers=3
)
print(chest_of_drawers)
table = f.make(
    furniture="table",
    material="oak",
    width=70,
    height=75,
    depth=130
)
print(table)