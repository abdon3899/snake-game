from turtle import Turtle

start_position = [ (0, 0) , (-20,0) , (-40,0) ]
move_distance = 20

up=90
down=270
left=180
right=0

class Snake:


    def __init__(self):
        self.segment=[]
        self.creat_snake()
        self.head = self.segment[0]

    def creat_snake(self):
        for position in start_position:
           self.add_segment(position)

    def add_segment(self,position):
        segment = Turtle("square")
        segment.pu()
        segment.color("white")
        segment.goto(position)
        self.segment.append(segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())



    def move(self):
        for segment_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segment_num - 1].xcor()
            new_y = self.segment[segment_num - 1].ycor()
            self.segment[segment_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000 ,1000)
        self.segment.clear()
        self.creat_snake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)



