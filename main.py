import turtle
import random

#Change the background color to black
turtle.bgcolor("black")

#Adjust speed of Turtle (lower=faster)
turtle.speed(0)

#List of colors
colors = ["#FF595E","#FFCA3A","#8AC926","#1982C4","#6A4C93"]

#Counter variables
color_num = 0
size = 1

#Change this variable to control how many sides your shape will have
sides = 4

#Draw the spiraling shape
#This loops forever

while(True):
  color_num = color_num + 1
  for i in range(sides):
    turtle.forward(size)
    turtle.right(360/sides + 1)
    size = size + 1
  turtle.color(colors[color_num % 5])
    