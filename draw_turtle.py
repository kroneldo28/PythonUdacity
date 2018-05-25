import turtle

def draw_square(some_turtle):
	for x in range(0,4):
		some_turtle.forward(100)
		some_turtle.left(90)

def draw_triangle(some_turtle):
	for x in range(0,3):
		some_turtle.forward(100)
		some_turtle.right(60)

def draw_window():
	window = turtle.Screen()
	window.bgcolor("red")

	tom = turtle.Turtle()
	tom.shape("triangle")
	tom.color("green")
	tom.speed(1)
	draw_square(tom)

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.speed(1)
	angie.circle(90)

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(1)
	draw_triangle(brad)

	window.exitonclick()
draw_window()
