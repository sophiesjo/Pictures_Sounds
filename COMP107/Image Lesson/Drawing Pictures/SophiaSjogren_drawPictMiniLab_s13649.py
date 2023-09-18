#Mini-Lab: Drawing Pictures
#Sophie Sjogren
#4-7-20

#This program creates a blank canvas
def drawAPict(width, height, color):
    pict = makeEmptyPicture(width, height, color)
    show(pict)
#Without a third color parameter, the picture is white. If provided only one parameter, the program returns as an error because of inappropriate argument type. If provided more than three parameters, the program returns the same error because of inappropriate argument type. If parameters are in a different order, the program returns an error due to inappropriate argument value of correct type. 

#The location of the pixel in the bottom right corner, if w = width and h = height, is (w-1,h-1). The location of the pixel in the center is (w/2-1,h/2-1).

#This program draws on a blank canvas
def drawOnPict(width, height, color):
    pict = makeEmptyPicture(width, height, color)
    addLine(pict,25,25,50,50,yellow)
    addRect(pict,25,25,50,50,yellow)
    addText(pict,25,25,"Soph's art", blue)
    addLine(pict,75,25,50,50,yellow)
    addOval(pict,25,55,50,20,blue)
    addRectFilled(pict,45,45,10,10,pink)
    return pict 
#If "This is silly" is added at location (0,0), the words are cut off, but the bottoms of the "s" and "y" are still barely visible on the top. If location is at (1,20), the text is fully visible and starts against the left side. If location is at (w-1,0), the words are not visible, but a little pixle of color can be seen on the right side. If location is at (0,w-40), the text is visible, starts against the left side and is a little more than half way down the canvas.

#This function draws on an existing picture.
def drawOnGivenPict(pict):
    w = getWidth(pict)
    h = getHeight(pict)
    addLine(pict,w-20,h-20,50,50,yellow)
    addRect(pict,w-50,h-50,50,50,yellow)
    return pict 
