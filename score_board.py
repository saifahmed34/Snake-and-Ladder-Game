import turtle


class ScoreBoard:
    def __init__(self, x_start, y_start):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.pencolor("white")
        self.turtle.speed(0)
        self.x_start = x_start
        self.y_start = y_start

    def show(self, names, positions):
        self.turtle.clear()
        self.turtle.goto(self.x_start, self.y_start)
        entries = sorted(zip(positions, names),reverse=True)
        for i, (position, name) in enumerate(entries):
            display_text = f"{position}. {name}"
            self.turtle.write(display_text, font=("Arial", 16, "bold"))
            self.turtle.goto(self.x_start, self.y_start - (i + 1) * 30)

    def clear(self):
        self.turtle.clear()
