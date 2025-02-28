import turtle

turtle.Screen().bgcolor("Red")
turtle.Screen().setup(50,70)

polygon = turtle.Turtle()
num_of_side = 6
lenght = 50
angle = 360 / num_of_side

for i in range(num_of_side):
    polygon.forward(lenght)
    polygon.right(angle)

turtle.done()