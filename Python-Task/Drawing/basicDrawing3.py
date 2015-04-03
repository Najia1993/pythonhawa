from graphics import *
import random
import time

# Do some simple drawing
window = GraphWin("Visualisation", 300, 300)

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
data = datafile.readlines()

listofBoxes = []

for i in range(0,len(data), 2):
    first = int(float(data[i].strip())) *2
    second = int(float(data[i+2].strip())) *2
    print(str(first) + " and " + str(second))
    #x = float(line.strip())
    #-----------------------------------------------------------------
    #ball = Circle(Point(150,150), x) 
    #ball.setFill(color_rgb(255,255,0))
    #ball.draw(window)
    #-----------------------------------------------------------------
    box = Rectangle(Point(250,250),Point(first,second))
    box.setFill(color_rgb(0,0,0))
    box.setOutline(color_rgb(255,255,255))
    box.draw(window)
    time.sleep(0.50)

    #-----------------------------------------------------------------
    #text = Text(Point(150,150),"Hello")
    #text.draw(window)
    #time.sleep(0.50)
    #-----------------------------------------------------------------

while True:
    for box in listofBoxes:
        box.setOutline(color_rgb(random.randint(0,250),random.randint(0,250),random.randint(0,250)))
        

# Waits until the mouse is clicked before closing the window
window.getMouse()
