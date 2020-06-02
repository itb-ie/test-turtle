import turtle
import random

def draw_square(pen, l):
    pen.forward(l)
    pen.right(90)
    pen.forward(l)
    pen.right(90)
    pen.forward(l)
    pen.right(90)
    pen.forward(l)

def draw_roof(pen, l, h):
    pen.right(30)
    pen.forward(2*h)
    pen.right(60)
    pen.forward(l-2*h)
    pen.right(60)
    pen.forward(2 * h)

sc = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)

l = 200
h = 50

# main body of the house
pen.color("#ff0000", "#cc0000")
pen.begin_fill()
draw_square(pen, 200)
pen.end_fill()
pen.color("#ff0000", "#990000")
pen.begin_fill()
draw_roof(pen, 200, 50)
pen.end_fill()

pen.right(30)
pen.penup()
pen.forward(30)
pen.right(90)
pen.forward(70)
pen.right(180)
pen.pendown()

# the windows
pen.color("#ff0000", "#aaffff")
pen.begin_fill()
draw_square(pen, 50)
pen.end_fill()

pen.penup()
pen.left(90)
pen.forward(110)
pen.left(180)
pen.pendown()


pen.begin_fill()
draw_square(pen, 50)
pen.end_fill()

# draw the door
# position
pen.penup()
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(170)
pen.left(90)
pen.forward(70)

# draw
pen.color("#330000", "#770000")
pen.begin_fill()
pen.pendown()
pen.forward(60)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(100)
pen.end_fill()

# handle
pen.back(50)
pen.left(90)
pen.pensize(4)
pen.forward(7)
pen.back(7)
pen.pensize(1)
pen.right(90)
pen.forward(50)

# go make the sun
pen.speed(9)
pen.penup()
pen.goto(-300, 250)
pen.pendown()
pen.color("yellow", "yellow")
pen.begin_fill()
pen.circle(80)
pen.end_fill()
pen.color("yellow", "yellow")

pen.goto(-220, 250)
ray = 120
pen.pensize(5)
for i in range(36):
    pen.forward(ray)
    pen.backward(ray)
    pen.right(10)


# go make a tree
pen.speed(1)
pen.penup()
pen.color("#330000", "#550000")
pen.begin_fill()
pen.goto(-300, -l)
pen.left(180)
pen.pendown()
pen.forward(150)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(20)
pen.end_fill()


pen.color("#22dd22", "#22dd22")
pen.begin_fill()
pen.penup()
pen.goto(-330, -l+140)
pen.pendown()
pen.circle(40)
pen.end_fill()

pen.begin_fill()
pen.penup()
pen.goto(-290, -l+140)
pen.pendown()
pen.circle(44)
pen.end_fill()

pen.begin_fill()
pen.penup()
pen.goto(-310, -l+175)
pen.pendown()
pen.circle(35)
pen.end_fill()


# go make grass
pen.penup()
pen.color("green", "yellow")
pen.goto(-400, -l)
#pen.left(90)
sc.delay(0)
pen.hideturtle()
pen.speed(0)

for i in range(800//3):
    pen.left(90)
    l = random.randint(5,10)
    pen.forward(l)
    pen.back(l)
    pen.penup()
    pen.right(90)
    pen.forward(3)

    pen.pendown()


turtle.done()