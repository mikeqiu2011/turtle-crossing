import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()

screen.onkey(fun=player.move, key='Up')

game_is_on = True
i = 0
level = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    i += 1

    if i == 100:
        print('increase cars!!')
        car_manager.add_cars()
        i = 0

    car_manager.move_cars(level)

    if car_manager.is_collide(player.pos()):
        print('collison detected')
        game_is_on = False

    if player.is_win():
        print('you win')
        player.restart()
        level += 1
