import turtle

color=('red','yellow','green','cyan','pink','white','gray')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(25)
for i in range(300):
	t.color(color[i%6])
	t.forward(i*1.5)
	t.left(59)
	t.width(3)