#Space Shooter - Python
#Author - Ahmed Safa

import turtle
import os
import math
import random

#Graphics Setup

wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("background.gif")
wn.title("Space Shooter")


#Shapes Register

turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")

#Border Customize

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#Set the Score to 0

score = 0

#Drow the Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score : %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()
#Player Setup

player = turtle.Turtle()
player.color("green")
player.shape("player.gif")
#player.shapesize(0.2)
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 20

#Total of Enemies

number_of_enemies = 6

#Create an empty list/Array of enemies

enemies = []

#Add enemies to the list

for i in range(number_of_enemies):

	#Create Enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:

	enemy.color("yellow")
	enemy.shape("enemy.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100,250)
	enemy.setposition(x,y)

enemyspeed = 2


#player's bullet

bullet = turtle.Turtle()
bullet.color("green")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.3,0.3)
bullet.hideturtle()

bulletspeed = 40


#Bullet State
#Ready to Fire

bulletstate = "ready"



#Move Right/Left

def move_left():
	x = player.xcor()
	x -= playerspeed
	
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	
	if x > 280:
		x = 280
	player.setx(x)


#Fire Function

def fire_bullet():

	#Define bulletstate as a global if it needs changed
	global bulletstate

	if bulletstate == "ready":
		
		os.system("mpg123 fire.wav&")
		bulletstate = "fire"
		#Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition( x, y)
		bullet.showturtle()

def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False	


#Keyboard Input

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"Up")

#Game Loop

while True:

	for enemy in enemies:
		#Move Enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move Enemy back & down

		if enemy.xcor() > 280:

			#Move all enemies dowsn

			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change Enemy Direction	
				
			enemyspeed *= -1	
		
		if enemy.xcor() < -280:
			#Move all enemies dowsn

			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change Enemy Direction	

			enemyspeed *= -1	

			

		#Check for a collision between the Bullet and Enemy

		if isCollision(bullet,enemy):

			os.system("mpg123 blast.wav&")
			#Reset the Bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)

			#Reset the Enemy
			x = random.randint(-200, 200)
			y = random.randint(100,250)
			enemy.setposition(x,y)

			#Update the Score
			score += 5
			scorestring = "Score : %s" %score
			score_pen.clear()
			score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

		#Game Over
		if isCollision(player,enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")

			break	

	#Move the Bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"

	




#Exit

delay = raw_input("Press Enter to Quite.")
