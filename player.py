from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.penup()
		self.setheading(90)
		self.reset_position()
		self.finish_line = False


	def move(self):
		self.fd(MOVE_DISTANCE)
		if self.ycor() >= FINISH_LINE_Y:
			self.finish_line = True



	def reset_position(self):
		self.clear()
		self.goto(STARTING_POSITION)
		self.finish_line = False