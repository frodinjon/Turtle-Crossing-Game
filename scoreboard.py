from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.hideturtle()
		self.penup()
		self.goto(-200, 280)
		self.write_score()


	def write_score(self):
		self.clear()
		self.write(f"Level: {self.score}")
		pass


	def increase_score(self):
		self.score += 1
		self.write_score()

	def game_over(self):
		self.goto(0,0)
		self.write("GAME OVER", align="center", font=FONT)
		