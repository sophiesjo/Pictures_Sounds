# Midterm Section 3
#Sophie Sjogren
#5-4-20

#This function negates the red value of all pixels if the pixel's red value is less than 128
def negateLowRed(picture):
    newPict = duplicatePicture(picture)
    for x in range(getWidth(newPict)):
      for y in range(getHeight(newPict)):
        px = getPixel(newPict, x, y)
        r = getRed(px)
        if(r < 128):
          newR = 255-r
          setRed(px, newR)
    return newPict

#This function creates a colored empty picture with a given width, height, and color
def makeColoredEmptyPicture(width, height, color):
    canvas = makeEmptyPicture(width, height)
    for x in range(width):
      for y in range(height):
        px = getPixel(canvas, x, y)
        setColor(px, color)
    return canvas

#This function takes a picture and returns a new picture that has half the red value and double the blue value
def halfRedDoubleBlue(picture):
    newPict = duplicatePicture(picture)
    for x in range(getWidth(newPict)):
      for y in range(getHeight(newPict)):
        px = getPixel(newPict, x, y)
        r = getRed(px)
        b = getBlue(px)
        halfRed = r/2
        doubleBlue = b*2
        setRed(px, halfRed)
        setBlue(px, doubleBlue)
    return newPict

#This function takes width and height values and creates a black empty canvas. The top left quadrant is made blue and the bottom right quadrant is made red.
def blackBlueAndRed(width, height):
    canvas = makeEmptyPicture(width, height, black)
    halfWidth = width/2
    halfHeight = height/2
    for x in range(halfWidth):
      for y in range(halfHeight):
        px = getPixel(canvas, x, y)
        setColor(px, blue)
    for x in range(halfWidth, width):
      for y in range(halfHeight, height):
        px = getPixel(canvas, x, y)
        setColor(px, red)
    return canvas
        
        