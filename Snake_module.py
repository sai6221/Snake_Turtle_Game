from turtle import Turtle
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    
    def __init__(self):
        self.bodys=[]
        self.create_snake()
        self.head = self.bodys[0]
        
    def create_snake(self):
        X=0
        for i in range(3):
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.setposition(X,0)
            X=X-20
            self.bodys.append(body)
            
    def move(self):
        for i in range(len(self.bodys)-1,0,-1):
            x=self.bodys[i-1].xcor()
            y=self.bodys[i-1].ycor()
            self.bodys[i].goto(x,y)
#         self.bodys[0].forward(90)
        self.head.forward(MOVE_DISTANCE)  
        
    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)