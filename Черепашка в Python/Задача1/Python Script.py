import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 30

for i in range(7):
    t.forward(10*k)
    t.right(120)

t.up()

for x in range(-5, 20):
    for y in range(0, 20):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()
