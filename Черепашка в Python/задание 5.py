import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 30
for i in range(4):
    t.forward(10*k)
    t.right(90)
t.up()
t.forward(3*k)
t.left(90)
t.forward(5*k)
t.right(90)
t.down()
for i in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(12*k)
    t.right(90)
t.up()
for x in range(-5, 11):
    for y in range(0, 14):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()

#171 точка
