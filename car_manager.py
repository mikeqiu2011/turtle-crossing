import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(position)


class CarManager:
    def __init__(self):
        self.cars = []
        self.init_cars()

    def init_cars(self):
        for y in range(-200, 280, 20):
            x = random.randint(0, 400)
            car = Car((x, y))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def is_collide(self, position):
        is_collide = False

        for car in self.cars:
            if car.distance(position) < 30:
                is_collide = True

        return is_collide
