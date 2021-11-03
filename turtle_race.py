import turtle
import random


screen = turtle.Screen()
guess = screen.textinput("Turtle Race","Which color of the turtle will win?")


colors = ["red","cyan","purple","blue","green"]
turtles = []
position = -200
winner = ''


screen.tracer(0)
finish = turtle.Turtle("arrow")
finish.penup()
finish.goto(350,-300)
finish.left(90)
def forward():   
    finish.pendown()
    finish.forward(20)
    finish.penup()
    finish.forward(20)
for y in range(14):
    forward()
screen.tracer(1)
for i in range(5):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-350,position)
    position += 100
    turtles.append(new_turtle)


game_on = True
while game_on :
    for i in turtles:           
        i.forward(random.randint(0,10))
        if i.xcor() >= 350:
            winner = i.color()[1]
            game_on = False

            

            
if guess == winner:
    turtle.write(f"The winner is {winner}", move = False, align = "center", font = ('Times New Roman', 14, 'bold') )

else:
    turtle.write(f"The winner is {winner}.Better Luck Next Time", move = False, align = "center", font = ('Times New Roman', 14, 'bold'))
            
            
            
            
            
            
        
        
            
                    



