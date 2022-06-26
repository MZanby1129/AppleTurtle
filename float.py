import turtle
turtle.speed(0)
turtle.bgcolor("gray")
for i in range (200) :
	for c in ("red", "green", "blue", "cyan", "yellow", "pink", "white") :
		turtle.color(c)
		turtle.pensize(2)
		turtle.left(4)
		turtle.forward(200)
		turtle.left(90)
		turtle.forward(200)
		turtle.left(90)
		turtle.forward(200)
		turtle.left(90)
		turtle.forward(200)
		turtle.left(90)