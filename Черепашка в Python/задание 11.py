import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 30
for i in range(4):
    t.forward(4*5**0.5*k)
    t.right(150)
    t.forward(4*5**0.5*k)
    t.right(300)
t.up()
for x in range(-8, 17):
    for y in range(-14, 10):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()

#96 точек
