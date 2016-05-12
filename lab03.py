# lab03.py for Ellia La and Kerry Jones
# CS20, Spring 2016, Instructor: Phill Conrad
# Draw some initials using turtle graphics

import turtle
import math

def drawE (t,w,h):
    """
    draw the letter E using t as the turtle, w as the width, and h as the height
    """
    #draw the top horizontal line of the E
    t.setheading (0)
    t.forward(w)
    t.backward(w)
    #draw the first half of the vertical line of the E
    t.setheading(270)
    t.forward (h/2)
    #draw the middle horizontal line of the E
    t.setheading (0)
    t.forward (w)
    t.backward (w)
    #draw the second half of the vertical line of the E
    t.setheading (270)
    t.forward (h/2)
    #draw the bottom horizontal line of the E
    t.setheading (0)
    t.forward (w)

def drawL (t,w,h,s):
    """
    draw the letter L using t as the turtle, w as the width, h as the height, and s as the spacing between letters
    """
    #move the turtle up h and over s to make space between the E and the L
    t.up ()
    t.goto (t.pos()+(s,h))
    t.down ()
    #draw the vertical component of the L
    t.setheading (270)
    t.forward (h)
    #draw the horizontal component of the L
    t.setheading (0)
    t.forward (w)

def drawK (t,w,h,s):
    """
    draw the letter K using t as the turtle, w as the width, h as the height, and s as the spacing between letters
    """
    #move the turtle up h and over 2s to make space between the L and the K
    t.up ()
    t.goto (t.pos()+(2*s,h))
    t.down ()
    #draw the vertical component of the K
    t.setheading (270)
    t.forward (h)
    t.backward (h/2)
    #draw the diagonal lines for K by using pythagorean theorem
    t.goto (t.pos()+(w,-h/2))
    t.goto (t.pos ()+(-w,h/2))
    t.goto (t.pos ()+(w,h/2))

def drawJ (t,w,h,s):
    """
    draw the letter J using t as the turtle, w as the width, h as the height, and s as the spacing between letters
    """
    #move the turtle over s to make space between K and the J
    t.up ()
    t.goto (t.pos()+(s,0))
    t.down ()
    #draw the horizontal component of the J
    t.setheading (0)
    t.forward (w)
    t.backward (w/2)
    #draw half of the vertical component of the J
    t.setheading (270)
    t.forward (h-(w/4))
    #move the turtle to the left to draw a semicircle
    t.up ()
    t.goto (t.pos ()+(-w/2,0))
    t.down ()
    t.circle (w/4,180,30)

def drawEL (t,w,h,s):
    """
    draw the letters EL using t as the turtle, w as the width, h as the height, and s as the spacing between letter
    """
    #draw the top horizontal line of the E
    t.setheading (0)
    t.forward(w)
    t.backward(w)
    #draw the first half of the vertical line of the E
    t.setheading(270)
    t.forward (h/2)
    #draw the middle horizontal line of the E
    t.setheading (0)
    t.forward (w)
    t.backward (w)
    #draw the second half of the vertical line of the E
    t.setheading (270)
    t.forward (h/2)
    #draw the bottom horizontal line of the E
    t.setheading (0)
    t.forward (w)
    #move the turtle up h and over s to make space between the E and the L
    t.up ()
    t.goto (t.pos()+(s,h))
    t.down ()
    #draw the vertical component of the L
    t.setheading (270)
    t.forward (h)
    #draw the horizontal component of the L
    t.setheading (0)
    t.forward (w)
    
 

def drawKJ (t,w,h,s):
    """
    draw the letters KJ using t as the turtle, w as the width, h as the height, and s as the spacing between letter
    """
    #move the turtle up h and over 2s to make space between the L and the K
    t.up ()
    t.goto (t.pos()+(2*s,h))
    t.down ()
    #draw the vertical component of the K
    t.setheading (270)
    t.forward (h)
    t.backward (h/2)
    #draw the diagonal lines for K by using pythagorean theorem
    t.goto (t.pos()+(w,-h/2))
    t.goto (t.pos ()+(-w,h/2))
    t.goto (t.pos ()+(w,h/2))
    #move the turtle over s to make space between K and the J
    t.up ()
    t.goto (t.pos()+(s,0))
    t.down ()
    #draw the horizontal component of the J
    t.setheading (0)
    t.forward (w)
    t.backward (w/2)
    #draw half of the vertical component of the J
    t.setheading (270)
    t.forward (h-(w/4))
    #move the turtle to the left to draw a semicircle
    t.up ()
    t.goto (t.pos ()+(-w/2,0))
    t.down ()
    t.circle (w/4,180,30)
    

def drawELKJ (t,w,h,s):
    """
    draw the letters ELKJ using t as the turtle, w as the width, h as the height, and s as the spacing between letter
    """
 #draw the top horizontal line of the E
    t.setheading (0)
    t.forward(w)
    t.backward(w)
    #draw the first half of the vertical line of the E
    t.setheading(270)
    t.forward (h/2)
    #draw the middle horizontal line of the E
    t.setheading (0)
    t.forward (w)
    t.backward (w)
    #draw the second half of the vertical line of the E
    t.setheading (270)
    t.forward (h/2)
    #draw the bottom horizontal line of the E
    t.setheading (0)
    t.forward (w)
    #move the turtle up h and over s to make space between the E and the L
    t.up ()
    t.goto (t.pos()+(s,h))
    t.down ()
    #draw the vertical component of the L
    t.setheading (270)
    t.forward (h)
    #draw the horizontal component of the L
    t.setheading (0)
    t.forward (w)
    #move the turtle up h and over 2s to make space between the L and the K
    t.up ()
    t.goto (t.pos()+(2*s,h))
    t.down ()
    #draw the vertical component of the K
    t.setheading (270)
    t.forward (h)
    t.backward (h/2)
    #draw the diagonal lines for K by using pythagorean theorem
    t.goto (t.pos()+(w,-h/2))
    t.goto (t.pos ()+(-w,h/2))
    t.goto (t.pos ()+(w,h/2))
    #move the turtle over s to make space between K and the J
    t.up ()
    t.goto (t.pos()+(s,0))
    t.down ()
    #draw the horizontal component of the J
    t.setheading (0)
    t.forward (w)
    t.backward (w/2)
    #draw half of the vertical component of the J
    t.setheading (270)
    t.forward (h-(w/4))
    #move the turtle to the left to draw a semicircle
    t.up ()
    t.goto (t.pos ()+(-w/2,0))
    t.down ()
    t.circle (w/4,180,30)
    
Fred=turtle.Turtle ()
def go():
    """
    draw the letters ELKJ three times using t as the turtle, w as the width, h as the height, and s as the spacing between letter- each time with different width, height, spacing, and location
    """
    Fred.up ()
    Fred.goto (-150,130)
    Fred.down ()
    drawELKJ (Fred,20,30,20)
    Fred.up ()
    Fred.goto (-190,-150)
    Fred.down()
    drawELKJ (Fred,60,90,5)
    Fred.up ()
    Fred.goto (50,0)
    Fred.down ()
    drawELKJ (Fred,10,10,45)
