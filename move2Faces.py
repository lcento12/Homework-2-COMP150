from graphics import *
import time

def makeFace2(center, win):
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

def makeFace1(center, win):
    head2 = Circle(center, 25)
    head2.setFill("yellow")
    head2.draw(win)

    eye2Center = center.clone() # face positions are relative to the center
    eye2Center.move(-10, 5)     # locate further points in relation to others
    eye2 = Circle(eye2Center, 5)
    eye2.setFill('blue')
    eye2.draw(win)

    eye3End1 = eye2Center.clone()
    eye3End1.move(15, 0)
    eye3End2 = eye3End1.clone()
    eye3End2.move(10, 0)
    
    eye4 = Line(eye3End1, eye3End2)
    eye4.setWidth(3)
    eye4.draw(win)

    mouthCorner3 = center.clone()
    mouthCorner3.move(-10, -10)
    mouthCorner4 = mouthCorner3.clone()
    mouthCorner4.move(20, -5)
    
    mouth2 = Oval(mouthCorner3, mouthCorner4)
    mouth2.setFill("red")
    mouth2.draw(win)

    noseCorner4 = center.clone()
    noseCorner4.move(-2,-2)
    noseCorner5 = center.clone()
    noseCorner5.move(2,-2)
    noseCorner6 = center.clone()
    noseCorner6.move(0,0)
    vertices1 = [noseCorner4, noseCorner5, noseCorner6]

    nose1 = Polygon(vertices1)
    nose1.setFill('red')
    nose1.draw(win)

    return [head2, eye2, eye4, mouth2, nose1]

def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp()
    
    faceList = makeFace1(Point(40, 100), win)
    faceList2 = makeFace2(Point(150,125), win)


    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .01
    for i in range(3):
        moveAll(faceList, dx, dy, stepsAcross, wait)
        moveAll(faceList2, -dx, dy, stepsAcross//2, wait)
    for shape in shapeList: 
        shape.move(dx, dy)
    


main()
