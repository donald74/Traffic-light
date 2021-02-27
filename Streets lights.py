# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:36:37 2021
Simulation Engineering

Assigment 12

@author: Obryl Donald Houaghon Nankap 523174 
"""
import numpy as np
import keyboard
from datetime import datetime
import time
import turtle


stp = turtle.Screen()
stp.title("Street lights simulation")
stp.bgcolor("black")

t = turtle.Turtle()
#the resolution of the screen
stp.setup(800,600)
#first class to define the light box on the second lane. 
class lightbox():
    def __init__(self, x, y):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("grey")
        self.pen.goto(x-30,y+60)
        self.pen.down()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.color = ""
        self.red_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()
        self.green_light = turtle.Turtle()
        self.red_light.speed(0)
        self.yellow_light.speed(0)
        self.green_light.speed(0)
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")
        self.red_light.shape("circle")
        self.yellow_light.shape("circle")
        self.green_light.shape("circle")
        self.red_light.penup()
        self.yellow_light.penup()
        self.green_light.penup()
        self.red_light.goto(x,y+40)
        self.yellow_light.goto(x,y)
        self.green_light.goto(x, y-40)
#function to change the color on light box      
    def light_change(self,color):
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")
        if color == "red":
            self.red_light.color("red")
            self.color = "red"
        elif color == "yellow":
            self.yellow_light.color("yellow")
            self.color = "yellow"
        elif color == "green":
            self.green_light.color("green")
            self.color = "green"
        else:
            print("Error {}".format(color))

#Here we define a second box witht new parameter of positon on screen.      
class lightbox2():
    def __init__(self, x, y):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("grey")
        self.pen.goto(x-10,y+70)
        self.pen.down()
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.color = ""
        self.red_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()
        self.green_light = turtle.Turtle()
        self.red_light.speed(0)
        self.yellow_light.speed(0)
        self.green_light.speed(0)
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")
        self.red_light.shape("circle")
        self.yellow_light.shape("circle")
        self.green_light.shape("circle")
        self.red_light.penup()
        self.yellow_light.penup()
        self.green_light.penup()
        self.red_light.goto(x+10,y+40)
        self.yellow_light.goto(x+50,y+40)
        self.green_light.goto(x+90, y+40)

    def light_change(self,color):
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")
        if color == "red":
            self.red_light.color("red")
            self.color = "red"
        elif color == "yellow":
            self.yellow_light.color("yellow")
            self.color = "yellow"
        elif color == "green":
            self.green_light.color("green")
            self.color = "green"
        else:
            print("Error {}".format(color))
            
#Here we delimit the limit of the road, to make your visual more understandable, and visible.
t.pensize(3)
t.pencolor("cyan")
t.penup()
t.goto(0,99)
t.pendown()
t.fd(-800)
t.fd(1800)
t.penup()
t.goto(57,-80)
t.pendown()
t.fd(800)
t.penup()
t.goto(57,-80)
t.pendown()
t.rt(90)
t.fd(500)
t.penup()
t.goto(-180,-80)
t.pendown()
t.fd(800)
t.penup()
t.goto(-180,-80)
t.pendown()
t.rt(90)
t.fd(800)

#Function for the click even on the second lane
def click(x, y):
    time.sleep(3)
    light2.light_change("yellow")
    light0.light_change("yellow")
    time.sleep(2)
    light2.light_change("red")
    light0.light_change("red")
    light1.light_change("green")
    t.fd(200)
    t.fd(100)
    t.rt(90)
    t.fd(399)
    time.sleep(3)
    light1.light_change("yellow")
    time.sleep(2)
    t.goto(0,-350)
    t.rt(-90)
    light1.light_change("red")
    light2.light_change("green")
    light0.light_change("green")


t.hideturtle()
t.penup()
t.fillcolor('gray')
t.goto(-200, -155)

t.begin_fill()
for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()

t.goto(-30,-200)

t.hideturtle()
t.pensize(10)
t.shapesize(2,2,1)
t.pencolor("pink")
t.penup()
t.goto(0,-350)
t.pendown()
t.penup()
t.showturtle()
t.left(-90)



light0 = lightbox2(85, 100)



light1 = lightbox(100, -150)
light1.light_change("red")


light2 = lightbox2(-300, -160)
light2.light_change("green")
light0.light_change("green")
stp.onclick(click)
stp.mainloop()

                