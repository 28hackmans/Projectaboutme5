import turtle
import random
screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("pink")
t = turtle.Turtle()

t.penup()
t.goto(0,0)
t.pendown()
t.write("All About Sammy", font=("arial", 30, "normal"), align="center")
t.fillcolor("purple")
t.begin_fill()
t.penup()
t.goto(0,100)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()
t.penup()
t.goto(100,-100)
t.pendown()
screen.addshape('flower2.gif')
t.shape('flower2.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(-100,-100)
t.pendown()
screen.addshape('flower1.gif')
t.shape('flower1.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(0,-250)
t.pendown()
t.write("Press Enter to Continue:", font=("arial", 30, "normal"), align="center")


round = input("Press Enter to continue: ")

t.clear()
screen.bgcolor("lavender")
t.penup()
t.goto(0,0)
t.pendown()
t.write("page 2", font=("arial", 30, "normal"), align="center")
t.clear()
t.penup()
t.goto(0,250)
t.pendown()
t.write("My favorite foods!", font=("arial", 30, "normal"), align="center")
t.penup()
t.goto(0,200)
t.pendown()
t.write("Tacos", font=("arial", 20, "normal"), align="center")
t.penup()
t.goto(0,150)
t.pendown()
t.write("Pasta", font=("arial", 20, "normal"), align="center")
t.penup()
t.goto(0,100)
t.pendown()
t.write("Olive Garden Salad", font=("arial", 20, "normal"), align="center")
t.penup()
t.goto(0,-50)
t.pendown()
t.fillcolor("hotpink")
t.begin_fill()
t.circle(40)
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(5)
t.end_fill()
t.penup()
t.goto(-200,0)
t.pendown()
screen.addshape('pasta.gif')
t.shape('pasta.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(200,0)
t.pendown()
screen.addshape('tacos.gif')
t.shape('tacos.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(0,-200)
t.pendown()
screen.addshape('salad.gif')
t.shape('salad.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0,-350)
t.pendown()
t.write("Press Enter to Continue:", font=("arial", 30, "normal"), align="center")

round = input("Press Enter to continue: ")

t.clear()
screen.bgcolor("lightblue")
t.penup()
t.goto(0,0)
t.pendown()
t.write("page 3", font=("arial", 30, "normal"), align="center")
t.clear()
t.penup()
t.goto(0,250)
t.pendown()
t.write("Hobbies", font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(0,200)
t.pendown()
t.penup()
t.write("Swimming", font=("arial", 20, "normal"), align="center")

t.goto(0,150)
t.pendown()
t.penup()
t.write("Gaming", font=("arial", 20, "normal"), align="center")

t.goto(0,100)
t.pendown()
t.penup()
t.write("Shopping", font=("arial", 20, "normal"), align="center")

t.penup()
t.goto(0,50)
t.pendown()
t.write("Hanging out with friends", font=("arial", 20, "normal"), align="center")

t.penup()
t.goto(150,0)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.goto(150,0)
t.goto(250,0)
t.goto(200,150)
t.goto(150,0)
t.end_fill()

t.penup()
t.goto(-150,-50)
t.pendown()
screen.addshape('swimmimg.gif')
t.shape('swimmimg.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(70,-150)
t.pendown()
screen.addshape('gaming.gif')
t.shape('gaming.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0,-300)
t.pendown()
t.write("Press Enter to Continue:", font=("arial", 30, "normal"), align="center")
round = input("Press Enter to continue: ")

t.clear()
screen.bgcolor("lightyellow")
t.penup()
t.goto(0,-25)
t.pendown()
t.fillcolor("lightpink")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

t.penup()
t.goto(0,250)
t.pendown()
t.write("Favorite TV Show", font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(0,150)
t.pendown()
t.write("Outer Banks", font=("arial", 20, "normal"), align="center")

t.penup()
t.goto(100,-100)
t.pendown()
screen.addshape('fam.gif')
t.shape('fam.gif')
t.stamp()
t.shape('classic')
t.penup()
t.goto(-100,-100)
t.pendown()
screen.addshape('obx.gif')
t.shape('obx.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0,-250)
t.pendown()
t.write("Press Enter to Continue:", font=("arial", 30, "normal"), align="center")
round = input("Press Enter to continue: ")

t.clear()
screen.bgcolor("orange")
t.penup()
t.goto(0,250)
t.pendown()
t.write("Favorite Sport", font=("arial", 30, "normal"), align="center")

t.penup()
t.goto(0,150)
t.pendown()
t.write("Hockey", font=("arial", 20, "normal"), align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("green")
t.pensize(8)
t.goto(-200,-100)
t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("purple")
t.fillcolor("purple")
t.begin_fill()

t.circle(25)
t.setheading(90)
t.circle(25)
t.setheading(180)
t.circle(25)
t.setheading(270)
t.circle(25)

t.end_fill()

t.fillcolor("yellow")
t.begin_fill()

t.penup()
t.goto(-200,-15)
t.pendown()
t.setheading(0)
t.circle(15)
t.end_fill()

t.penup()
t.goto(-50,-100)
t.pendown()
screen.addshape('pens.gif')
t.shape('pens.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(150,-100)
t.pendown()
screen.addshape('hockey.gif')
t.shape('hockey.gif')
t.stamp()
t.shape('classic')

turtle.done()
