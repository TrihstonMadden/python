# plot-dictionary.py
import tkinter as tk
import turtle

def main():
	#table is a dictionary
	table = {-100:0,-90:10,-80:20,-70:30,-60:40,-50:50,
				-40:40,-30:30,-20:20,-10:10,0:0,
					10:10,20:20,30:30,40:40,50:50,
					60:40,70:30,80:20,90:10,100:0,
					
					
			}
	print(" KEYS ")
	print(table.keys())
	print(" VALUES ")
	print(table.values())
	#turtle graphics
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#tWin = turtle.Screen()
	for h,k in table.items():  #get the items in the dictionary
		print(h, k) # trace code
		#x,y = table[n]
		t.speed(.5)
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(5)
	twin.exitonclick()

main()

"""
This code uses a dictionary with keys ranging from
-100 to 100 incrementing by 10.
Each key has a value of 0 as an integer.
To retrieve the values in the dictionary "table" a for loop is used.
The x cooridate on a python turtle screen corresponds to h while
the y value cooresponds to k.
**************************************
for h,k in table.items():  #get the items in the dictionary
		print(h, k) #trace code
h and k are then ploted using
		t.goto(h,k)
		t.pendown()
		t.circle(5)

Change the values from 0 to another integer.
Try to make something grovey.
"""
