from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        """Creating the Turtle Screen and initializing every element in the game"""
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Krall's Pong")
        self.screen.tracer(0)
        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))
        self.ball = Ball()
        self.scoreboard = Scoreboard()

    def control(self):
        """Up and Down arrows are controlling the right paddle, w and s are controlling the right one"""
        self.screen.listen()
        self.screen.onkey(self.r_paddle.paddle_up, "Up")
        self.screen.onkey(self.r_paddle.paddle_down, "Down")
        self.screen.onkey(self.l_paddle.paddle_up, "w")
        self.screen.onkey(self.l_paddle.paddle_down, "s")

    def run(self):
        """Main method running the game"""
        game_running = True
        while game_running:
            time.sleep(self.ball.move_speed)
            self.control()
            self.screen.update()
            self.ball.move()
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                # bouncing against top or bottom wall
                self.ball.bounce_y()
            if (self.ball.distance(self.r_paddle) < 50 and self.ball.xcor() > 320) or \
                    (self.ball.distance(self.l_paddle) < 50 and self.ball.xcor() < -320):
                # a player's paddle touched the ball
                self.ball.bounce_x()
                self.ball.move_speed *= 0.9
            if self.ball.xcor() > 380:
                # Right player missed it
                self.ball.reset_position()
                self.scoreboard.l_point()
            if self.ball.xcor() < - 380:
                # Left player missed it
                self.ball.reset_position()
                self.scoreboard.r_point()


if __name__ == '__main__':
    game = Game()
    game.run()
    game.screen.exitonclick()

