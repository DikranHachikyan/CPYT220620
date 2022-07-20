from draw import Point

class Rectangle(Point):
    
    def __init__(self, *, x=0, y=0, width=0, height=0):
        super().__init__( x=x, y=y)
        print('Init Rectangle')

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    # function override
    def draw(self):
        super().draw()
        print(f'rectangle:[{self.width} x {self.height}]')
