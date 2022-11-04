from graphics import *
win = GraphWin()

def sceneOne():
    win.setBackground('cyan')
    
    pt = Point (100, 100)
    
    cir = Circle(pt, 50)
    cir.draw(win)
    cir.setFill('pink')

    label = Text(Point(100,100), ':3')
    label.setTextColor('green')
    label.setSize(25)
    label.draw(win)

    label2 = Text(Point(25, 150), 'meow')
    label2.draw(win)

    win.getMouse()
    win.setBackground('blue')
    
    pt = Point (100, 100)
    
    cir1 = Circle(pt, 50)
    cir1.draw(win)
    cir1.setFill('pink4')

    label1 = Text(Point(100,100), ':3')
    label1.setTextColor('cyan')
    label1.setSize(25)
    label1.draw(win)
    label1.setStyle('bold')

    label12 = Text(Point(50, 150), 'meow (at night)')
    label12.draw(win)


sceneOne()
