import turtle

turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)
def func():
	for i in range(200):
		turtle.right(1)
		turtle.forward(1)
turtle.color('#fe7d7d','#fe7d7d')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
func()
turtle.right(240)
func()
turtle.forward(111.65)
turtle.end_fill()

turtle.done()