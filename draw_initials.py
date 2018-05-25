import turtle
import math

#def draw_k(pointer,size):
	
def open_square(pointer,size):
	for x in range(0,3):
		pointer.forward(size)
		pointer.right(90)

def draw_r(pointer,size):
	pointer.left(90)
	pointer.forward(size)
	pointer.right(90)
	x = size/2
	open_square(pointer,x)
	pointer.right(135)
	y = math.sqrt( (x*x)+(x*x) )
	pointer.forward(y)

def draw(size):
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(2)

	draw_r(brad,size)
	#TODO function to jump from one point to another to make a space
	#draw_k(brad,size)

	window.exitonclick()

draw(100)
