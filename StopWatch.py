import turtle
import time
import winsound
b=turtle.Turtle()
b.hideturtle()
b.speed(5)

s=turtle.Screen()
s.bgcolor("black")
b.pensize(10)
b.pencolor("white")
b.penup()
b.goto(-150,30)
b.pendown()
b.write("STOP WATCH",font=("Arial rounded MT bold",30,""))
def watch(x,y,z):

    t.penup()  
    t.goto(130,-130)  
    t.pendown()  
    t.write(x,font=("Arial",30,""))
 

    t.penup()  
    t.goto(-10,-130)  
    t.pendown()  
    t.write(y,font=("Arial",30,"")) 
  
    t.penup()  
    t.goto(-150,-130)  
    t.pendown()  
    t.write(z,font=("Arial",30,""))  
  
    t.penup()  
    t.goto(130,-130)

b.penup()
b.goto(-200,0)
b.pendown()
b.fd(400)
b.setheading(270)
b.fd(200)
b.setheading(180)
b.fd(400)
b.setheading(90)
b.fd(200)
b.penup()
b.goto(-80,-130)
b.pendown()
b.write(":",font=("Arial",30,""))
b.penup()
b.goto(60,-130)
b.pendown()
b.write(":",font=("Arial",30,""))
b.penup()

b.goto(-150,-70)
b.pendown()
b.pencolor("cyan")
b.write("Hrs",font=("Arial rounded MT bold",10,""))
b.penup()

b.goto(-10,-70)
b.pendown()
b.pencolor("cyan")
b.write("Mins",font=("Arial rounded MT bold",10,""))
b.penup()

b.goto(130,-70)
b.pendown()
b.write("Secs",font=("Arial rounded MT bold",10,""))

t=turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(0)
t.pencolor("green")
sec=0
hrs=0
mins=0

while True:
    watch(sec,mins,hrs)
    sec+=1
    
    winsound.Beep(1000,10)
    time.sleep(1)
    t.clear()
    if(sec==60):
        mins+=1
        sec=0
    if(mins==60):
        hrs+=1
        mins=0    
turtle.done()