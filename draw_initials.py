import turtle
import math

def draw_k(pointer,size):
	pointer.left(90)
	pointer.forward(size)
	x = size/2
	pointer.backward(x)	
	pointer.right(45)
	y = math.sqrt((x*x)+(x*x))
	pointer.forward(y)
	pointer.backward(y)
	pointer.right(90)
	pointer.forward(y)
	#Bring back the pen to its original angle
	pointer.left(45)
	
	
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
	#Bring back the pen to its original angle
	pointer.left(45)

#function to jump from one point to another to make a space
def space(pointer):	
	pointer.penup()
	pointer.forward(10)
	pointer.pendown()

def draw(size):
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(1)

	draw_r(brad,size)
	space(brad)
	draw_k(brad,size)

	window.exitonclick()

draw(100)
