#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        for end in range(self.y):
            print()
        for row in range(self.height):
            for elem in range(self.width + self.x):
                if elem < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        if args and args is not None:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            else:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'height':
                    self.height = value
                elif key == 'width':
                    self.width = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        my_dict = {}
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        my_dict['id'] = self.id
        my_dict['height'] = self.height
        my_dict['width'] = self.width
        return my_dict
