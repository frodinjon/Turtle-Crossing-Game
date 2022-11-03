from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_RANGE = [-250, 250]


class CarManager(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("square")
		self.move_dist = STARTING_MOVE_DISTANCE
		self.shapesize(stretch_wid = 1, stretch_len = 2)
		self.penup()
		self.setheading(180)
		self.color(random.choice(COLORS))
		self.position = (300, random.randint(Y_RANGE[0], Y_RANGE[1]))
		self.goto(self.position)


	def move(self):
		self.fd(self.move_dist)


	def increase_speed(self):
		self.move_dist += 5

	def __del__(self):
		self.hideturtle()
		del self