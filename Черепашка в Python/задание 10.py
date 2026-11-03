import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 30
for i in range(2):
    t.forward(20*k)
    t.right(90)
    t.forward(9*k)
    t.right(90)
t.up()
t.forward(12.5*k)
t.right(90)
t.down()
for i in range(2):
    t.forward(20*k)
    t.right(90)
    t.forward(9*k)
    t.right(90)
t.up()
for x in range(0, 25):
    for y in range(0, 22):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()
