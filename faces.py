from graphics import *
import time

win = GraphWin()

def makeFace(center, win):
    '''display face centered at center in window win.
    Return a list of the shapes in the face. '''
  
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

    face = [head, eye1, eye2, mouth, nose]

    for i in range(6):
        win.getMouse()
        win.yUp()
        return face
    


makeFace(center, win)
