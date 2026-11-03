import turtle
screen = turtle.Screen()
t = turtle.Turtle()
def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
turtle.colormode(255)
mycircle(255, 0, 0)
turtle.done()
