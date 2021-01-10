import math


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'


class Rectangle:
    '''
    Represents a 2D rectangle in a plane
    '''
    def __init__(self, p1, p2, colour):
        '''(Rectangle, num, num, str) -> None'''
        self.p1 = p1
        self.p2 = p2
        self.colour = colour

    def get_bottom_left(self):
        '''(Rectangle) -> num'''
        return self.p1

    def get_top_right(self):
        '''(Rectangle) -> num'''
        return self.p2

    def get_colour(self):
        '''(Rectangle) -> str'''
        return self.colour

    def reset_colour(self, colour):
        '''(Rectangle, str) -> None'''
        self.colour = colour

    def get_perimeter(self):
        '''(Rectangle) -> num'''
        x1, y1 = self.p1.get()
        x2, y2 = self.p2.get()
        length = (x2 - x1)
        width = (y2 - y1)
        return 2 * (width + length)

    def get_area(self):
        '''(Rectangle) -> num'''
        x1, y1 = self.p1.get()
        x2, y2 = self.p2.get()
        length = (x2 - x1)
        width = (y2 - y1)
        return width * length

    def move(self, x, y):
        '''(Rectangle, num, num) -> None'''
        self.p1.move(x, y)
        self.p2.move(x, y)

    def intersects(self, rectangle):
        '''(Rectangle, Rectangle) -> bool'''
        if self.p2.x < rectangle.p1.x or rectangle.p2.x < self.p1.x:
            return False
        if self.p2.y < rectangle.p1.y or rectangle.p2.y < self.p1.y:
            return False
        return True

    def contains(self, x, y):
        """(Rectangle, num, num) -> bool"""
        if (self.p1.x <= x) and (self.p2.x >= x):
            if (self.p1.y <= y) and (self.p2.y >= y):
                return True

    def __eq__(self, other):
        """(Rectangle, Rectangle) -> bool"""
        return self.p1 == other.p1 and self.p2 == other.p2 and self.colour == other.colour

    def __repr__(self):
        """(Rectangle) -> str"""
        return "Rectangle(" + repr(self.p1) + "," + repr(self.p2) + "," + repr(self.colour) + ")"

    def __str__(self):
        """(Rectangle) -> str"""
        return 'I am a ' + self.colour + ' rectangle with bottom left corner at (' + str(self.p1.x) + ',' + str(
            self.p1.y) + ') and top right corner at (' + str(self.p2.x) + ',' + str(self.p2.y) + ')'


class Canvas:
    """The space with multiple 2d rectangles"""
    def __init__(self, c=[]):
        """(Canvas, lst) -> None"""
        self.c = c

    def add_one_rectangle(self, rectangle):
        """(Canvas, Rectangle) -> None"""
        self.c.append(rectangle)

    def count_same_colour(self, colour):
        """(Canvas, str) -> num"""
        num1 = 0
        for i in self.c:
            if i.colour == colour:
                num1 += 1
            return num1

    def total_perimeter(self):
        """(Canvas) -> num"""
        perim = 0
        for i in self.c:
            perim += i.get_perimeter()
        return perim

    def min_enclosing_rectangle(self):
        """(Canvas) -> Rectangle"""
        minx = 100000
        maxx = -100000
        miny = 100000
        maxy = -100000
        for r in self.c:
            if minx > r.p1.x:
                minx = r.p1.x
            if maxx < r.p2.x:
                maxx = r.p2.x
            if miny > r.p1.y:
                miny = r.p1.y
            if maxy < r.p2.y:
                maxy = r.p2.y
        rectangle = Rectangle(Point(minx, miny), Point(maxx, maxy), "red")
        return repr(rectangle)

    def common_point(self):
        """(Canvas) -> Bool"""
        for i in self.c:
            for k in self.c:
                if not i.intersects(k):
                    return False
        return True

    def __len__(self):
        """(Canvas) -> num"""
        return len(self.c)

    def __repr__(self):
        """(Canvas) -> str"""
        strang = "Canvas("
        for i in self.c:
            strang += repr(i) + ","
            strang = strang[:-1]
            strang += ")"
        return strang



