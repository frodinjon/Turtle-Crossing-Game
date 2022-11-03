import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
cars = []



screen.onkey(fun=player.move, key="Up")
screen.listen()

game_is_on = True
game_turn = 0
while game_is_on: 
	time.sleep(0.1)
	screen.update() 
	game_turn += 1
	for car in cars:
		car.move()
		if car.xcor() < -500:
			car.__del__()
			cars.remove(car)
			#cars.remove(car)
			#del car
	if game_turn % 6 == 0:
		car = CarManager()
		cars.append(car)

	if player.finish_line == True:
		player.reset_position()
		scoreboard.increase_score()
		for car in cars:
			car.increase_speed()

	else:
		for car in cars:
			if player.distance(car) < 20:
				game_is_on = False
				scoreboard.game_over()
		



screen.exitonclick()