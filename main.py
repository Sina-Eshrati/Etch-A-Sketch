from turtle import Turtle, Screen

my_turtle = Turtle()


def forward():
    my_turtle.forward(10)


def backward():
    my_turtle.backward(10)


def turn_right():
    my_turtle.right(5)


def turn_left():
    my_turtle.left(5)


def clear():
    my_turtle.reset()


my_screen = Screen()
my_screen.listen()
my_screen.onkey(forward, 'w')
my_screen.onkey(backward, 's')
my_screen.onkey(turn_right, 'd')
my_screen.onkey(turn_left, 'a')
my_screen.onkey(clear, 'c')
my_screen.exitonclick()
