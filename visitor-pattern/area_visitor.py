# The Visitor pattern is a way of separating an algorithm from an object structure on which it operates.

# Elements
class Circle():
  def __init__(self, radius):
    self.radius = radius

  def accept(self, visitor):
    visitor.visit_circle(self)

class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def accept(self, visitor):
    visitor.visit_rectangle(self)

class Square():
  def __init__(self, side):
    self.side = side

  def accept(self, visitor):
    visitor.visit_square(self)

# Visitor
class Visitor():
  def visit_circle(self, circle):
    pass

  def visit_rectangle(self, rectangle):
    pass

  def visit_square(self, square):
    pass

class AreaVisitor():
  def visit_circle(self, circle):
    print('Area of circle is', 3.14 * circle.radius * circle.radius)

  def visit_rectangle(self,rectangle):
    print('Area of rectangle is', rectangle.width * rectangle.height)

  def visit_square(self, square):
    print('Area of square is', square.side * square.side)

class PerimeterVisitor():
  def visit_circle(self, circle):
    print('Perimeter of circle is', 2 * 3.14 * circle.radius)

  def visit_rectangle(self,rectangle):
    print('Perimeter of rectangle is', 2 * (rectangle.width + rectangle.height))

  def visit_square(self, square):
    print('Perimeter of square is', 4 * square.side)

# ==============================================
# Usage
# ==============================================
circle = Circle(3)
rectangle = Rectangle(2, 3)

# Creating the visitors
area_visitor = AreaVisitor()
perimeter_visitor = PerimeterVisitor()

# Accepting the area visitor
circle.accept(area_visitor)
rectangle.accept(area_visitor)

# Accepting the perimeter visitor
circle.accept(perimeter_visitor)
rectangle.accept(perimeter_visitor)
