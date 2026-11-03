import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 30
for i in range(5):
    t.right(45)
    t.forward(10*k)
    t.right(45)
for i in range(6):
    t.forward(20*k)
    t.right(90)
t.up()
for x in range(0, 28):
    for y in range(-13, 8):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()
