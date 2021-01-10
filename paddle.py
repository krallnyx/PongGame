from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        """Initialise a paddle at Position (as a (x, y) tuple)"""
        super().__init__()
        self.penup()
        self.goto(pos)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def paddle_up(self):
        """Moves the paddle up by 20 px"""
        self.goto(self.xcor(), self.ycor() + 20)

    def paddle_down(self):
        """Moves the paddle down by 20 px"""
        self.goto(self.xcor(), self.ycor() - 20)
