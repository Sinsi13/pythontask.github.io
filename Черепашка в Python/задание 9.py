import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 30
for i in range(5):
    t.forward(18*k)
    t.right(90)
    t.forward(3*k)
t.up()
for x in range(0, 22):
    for y in range(-4, 20):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()

#18
