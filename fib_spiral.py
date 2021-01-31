
#Final code to print the fibonacci spiral
from turtle import *
import math

#fib_arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] #automate

fib_arr = [1]

# Function to print first n
# Fibonacci Numbers

def getFibNumbers(n):

	f1 = 0
	f2 = 1
	if (n < 1):
		return
	print(f1, end=" ")
	for x in range(1, n):
		#print(f2, end=" ")
            fib_arr.append(f2)
            print(f2)
            next_num = f1 + f2
            f1 = f2
            f2 = next_num
        

n = int(input('Enter the number of iterations (must be > 1): ')) 
getFibNumbers(n)

def draw_square(side_length):  #Function for drawing a square
    for i in range(4):
        forward(side_length)
        right(90) #will move by 90 deg, i.e. line will appear as right angle

nr_squares=len(fib_arr) #num of squares


factor = 3                         #Magnifying factor
penup()
goto(50,50)                       #Move starting point right and up
pendown()

for i in range(nr_squares):
    draw_square(factor*fib_arr[i]) #Draw square
    penup()                        #Move to new corner as starting point
    forward(factor*fib_arr[i])
    right(90)                      #Turn turtle right by angle units,used to draw adjacent squares
    forward(factor*fib_arr[i])
    pendown()

penup()
goto(50,50)       #Move to starting point
setheading(0)   #Face the turtle to the right
pencolor('red')
pensize(3)
pendown()
#Draw quartercircles with fibonacci numbers as radius
for i in range(nr_squares):
    circle(-factor*fib_arr[i],90)  # minus sign to draw clockwise

exitonclick()