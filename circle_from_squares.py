import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_shape():
    window=turtle.Screen()
    window.bgcolor("red")


            
    brad = turtle.Turtle()
            
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(100)

    for f in range(36):
        draw_square(brad)
        brad.right(10)



    window.exitonclick()

    
draw_shape()
