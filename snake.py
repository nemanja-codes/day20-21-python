from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for segment_index in range(3):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=STARTING_POSITIONS[segment_index], y=0)
            self.snake_parts.append(new_segment)

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(x=new_x, y=new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)
