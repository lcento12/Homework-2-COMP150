'''Test animation of a group of objects making a face.
Combine the face elements in a function, and use it twice.
Have an extra level of repetition in the animation.

As in backAndForth2Flush.py, this version replaces moveAllOnLine by
moveAllOnLineFlush, to only update the screen once for each
animation step, after multiple individual graphics instructions are given.
'''

from graphics import *
import time

def moveAll(shapeList, dx, dy):
    ''' Move all shapes in shapeList by (dx, dy).'''    
    for shape in shapeList: 
        shape.move(dx, dy)
            

def moveAllOnLineUpdate(shapeList, dx, dy, repetitions, delay, win): 
    '''Animate the shapes in shapeList along a line in win.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    '''
    win.autoflush = False  
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        update()     
        time.sleep(delay)
    win.autoflush = True 
        

def makeFace(center, win):
    '''display face centered at center in window win.
    Return a list of the shapes in the face.
    '''
    
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1Center = center.clone() # face positions are relative to the center
    eye1Center.move(-10, 5)     # locate further points in relation to others
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    noseCorner1 = center.clone()
    noseCorner1.move(-2,-2)
    noseCorner2 = center.clone()
    noseCorner2.move(2,-2)
    noseCorner3 = center.clone()
    noseCorner3.move(0,0)
    vertices = [noseCorner1, noseCorner2, noseCorner3]

    nose = Polygon(vertices)
    nose.setFill('red')
    nose.draw(win)

    
    return [head, eye1, eye2, mouth, nose]

def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp() # make right side up coordinates!


    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    faceList = makeFace(Point(40, 100), win)
    faceList2 = makeFace(Point(150,125), win)

    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .05
    for i in range(3):                          
        moveAllOnLineUpdate(faceList, dx, 0, stepsAcross, wait, win)
        moveAllOnLineUpdate(faceList, -dx, dy, stepsAcross//2, wait, win)
        moveAllOnLineUpdate(faceList, -dx, -dy, stepsAcross//2, wait, win)

    win.promptClose(win.getWidth()/2, 20)

main()
