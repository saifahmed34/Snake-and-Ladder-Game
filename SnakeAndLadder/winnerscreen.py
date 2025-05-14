from turtle import Screen, Turtle


class WinnerScreen:
    def __init__(self):
        self.screen = Screen()

    def show_winner(self, winner_color):
        self.screen.clear()
        self.screen.bgcolor('black')
        winner = Turtle()
        winner.color(winner_color)
        winner.penup()
        winner.goto(0, 0)
        winner.hideturtle()
        winner.pencolor('white')
        winner.write(f"the winner is {winner_color}", align="center", font=("Courier", 50, "bold"))
