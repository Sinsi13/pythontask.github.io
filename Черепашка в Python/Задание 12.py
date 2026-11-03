import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 30
for i in range(8):
    t.right(45)
    t.forward(8*k)
t.up()
for x in range(0, 23):
    for y in range(-14, 10):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()

#19 точек
