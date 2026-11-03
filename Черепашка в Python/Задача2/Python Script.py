import turtle as t #подключаем модуль "черепаха"
t.tracer(0) #отключение анимации черепахи
t.left(90) #поворачивает черепаху на 90 градусов влево
t.screensize(10000, 10000) #масштаб
p = 1
k = 50 #коэффициент увеличения
#построение фигуры
for i in range(4):
    t.forward(12*k)
    t.right(90)
    t.right(30)
for i in range(3):
    t.forward(8*k)
    t.right(60)
    t.forward(8*k)
    t.right(120)
#поднимаем перо чтобы не рисовать линии
t.up()
#алгоритм построения точек
for x in range(-5, 20):
    for y in range(0, 20):
        t.goto(x*k, y*k)
        t.dot(4, "red") #рисует точки размером 5 красного цвета
t.update() #обновляет экран при использовании команды tracer
t.done() #завершение программы
