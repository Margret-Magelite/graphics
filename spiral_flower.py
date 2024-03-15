import turtle as m

m.title('SpiralFlower')
m.bgcolor('black')
m.pencolor('yellow')
m.speed(1000)
m.width(5)

def form(i):
    m.circle(100,i)
    m.penup()
    m.goto(0, 0)
    m.pendown()
    m.circle(-100, i)

def flower():
    for _ in range (0, 120, 6):
        form(_)

flower()
m.setheading(90)
flower()
m.setheading(180)
flower()
m.setheading(270)
flower()
m.exitonclick()
m.done()