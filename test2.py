import turtle

#메인 함수
def function():
    for i in range(1,150):
        y = (i**2+1)*0.01
        turtle.goto(i,y)

#x,y축을 그리는 함수
def axis():
    t.left(90)
    t.forward(300)
    t.penup()
    t.left(180)
    t.forward(300)
    t.pendown()
    t.left(90)
    t.forward(300)

y  = 0

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.pensize(2)

axis()
function()