from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """Create a white circle ball moving towards the up right corner"""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Updates the position of the ball, accordingly to the x_move and y_move"""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        """Reverse the move of the ball on the y axe"""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the move of the ball on the x axe"""
        self.x_move *= -1

    def reset_position(self):
        """Reset the position of the ball and invert its x axe"""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
