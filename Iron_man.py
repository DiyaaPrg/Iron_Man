# Importing modules
import turtle
import coordinates
from coordinates import face_one, face_two, face_three
import time

# Hide the cursor:
turtle.hideturtle()

# Set the background color:
turtle.bgcolor("red")

# Set the window size: width & height in pixels:
turtle.setup(500, 600)

# Set the drawing speed:
turtle.speed(2)

face_one_start = (-40, 120)
face_two_start = (-40, -30)
face_three_start = (-60, -220)


# Function to draw the three faces:
def draw_face(face_start, face):
    turtle.penup()
    turtle.goto(face_start)
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.pendown()

    for i in range(len(face[0])):
        x, y = face[0][i]
        turtle.goto(x, y)
        time.sleep(1)

    for i in range(len(face[1])):
        x, y = face[1][i]
        turtle.goto(x, y)
        time.sleep(1)

    turtle.end_fill()


draw_face(face_one_start, coordinates.face_one)
draw_face(face_two_start, coordinates.face_two)
draw_face(face_three_start, coordinates.face_three)


turtle.exitonclick()


