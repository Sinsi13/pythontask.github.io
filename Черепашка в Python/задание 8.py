import turtle as t
t.tracer(0)
t.left(90)
t.screensize(10000, 10000)
k = 15
t.right(45)
for i in range(10):
    t.right(45)
    t.forward(203*k)
    t.right(45)
t.up()
t.backward(40*k)
t.right(45)
t.down()
for i in range(5):
    t.forward(20*k)
    t.left(90)
t.up()
for x in range(0, 235):
    for y in range(-204, 1):
        t.goto(x*k, y*k)
        t.dot(4, "red")
t.update()
t.done()    

#1 квадрат = 40 804
#2 квадрат = 400
#41 204
