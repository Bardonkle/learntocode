
class Shape:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name

    def is_circle(self):
        if self.sides == 0:
            return True 
        else:
            return False

square = Shape(4, "square")
circle = Shape(0, "circle")

num_sides = square.sides
circle_sides = circle.sides

result = square.is_circle()
print("square is a circle: ", result)

result = circle.is_circle()
print("circle is a circle: ", result)

print(num_sides)


class Computer:

    def __init__(self, cpu, gpu, price):
        self.cpu = cpu
        self.gpu = gpu
        self.price = price
        self.is_on = False
    
    def turn_on_computer(self):
        self.is_on = True

    def turn_off_computer(self):
        self.is_on = False

my_pc = Computer("ryzen", "1660", "1k")

my_pc.turn_on_computer()
print(my_pc.is_on)

my_pc.turn_off_computer()
print(my_pc.is_on)