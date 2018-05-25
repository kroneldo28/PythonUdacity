import turtle

def draw_square(some_turtle):
	for x in range(0,4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(1)

	for x in range(0,36):
		draw_square(brad)
		brad.right(10)
	
	window.exitonclick()
	
draw()
