#!/usr/bin/python3
"""
import the class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square inherited of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ define the__init__ constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Display the properties of the rectangle """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """ define the size property """
        return self.width

    @size.setter
    def size(self, value):
        """ define the size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ define the update method """
        if args and args is not None:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            else:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ define the dictionary method """
        my_dict2 = {}
        my_dict2['id'] = self.id
        my_dict2['x'] = self.x
        my_dict2['size'] = self.size
        my_dict2['y'] = self.y
        return my_dict2
