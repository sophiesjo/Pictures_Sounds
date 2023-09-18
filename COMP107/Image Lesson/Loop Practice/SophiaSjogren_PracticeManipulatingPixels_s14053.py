#Mini-Lab: More Practice with For Loops for Manipulating Pixels in a Picture
#Sophie Sjogren
#4-15-20

#Draws a white horizontal line across the top of a picture
def makeWhiteLine(picture):
    newPict = duplicatePicture(picture)
    for x in range(getWidth(newPict)):
      px = getPixel(newPict, x, 1)
      setColor(px, white)
    return newPict

#Draws a horizontal line across the top of a picture with the given color
def makeColoredLine(picture, color):
    newPict = duplicatePicture(picture)
    for x in range(getWidth(newPict)):
      px = getPixel(newPict, x, 1)
      setColor(px, color)
    return newPict
    
#Draws a horizontal line across the given row of a picture with the given color
def makeHorizontalLine(picture, color, row):
    newPict = duplicatePicture(picture)
    for x in range(getWidth(newPict)):
      px = getPixel(newPict, x, row)
      setColor(px, color)
    return newPict

#Draws a vertical line across the given column of a picture with the given color
def makeVerticalLine(picture, color, column):
    newPict = duplicatePicture(picture)
    for y in range(getHeight(newPict)):
      px = getPixel(newPict, column, y)
      setColor(px, color)
    return newPict

#Fills the entire picture with a given color
def colorAll(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(getHeight(newPict)):
      for x in range(getWidth(newPict)):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict
    
#Fills the left half of a picture with a given color
def colorLeft(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(getHeight(newPict)):
      for x in range(getWidth(newPict)/2):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict
    
#Fills the top half of a picture with a given color
def colorTop(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(getHeight(newPict)/2):
      for x in range(getWidth(newPict)):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict

#Fills the upper left quadrant of a picture with a given color
def colorQuadrant(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(getHeight(newPict)/2):
      for x in range(getWidth(newPict)/2):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict
    
#Fills every other row of a picture with a given color
def colorEveryOtherRow(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(0, getHeight(newPict), 2):
      for x in range(getWidth(newPict)):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict

#Fills every other column of a picture with a given color
def colorEveryOtherColumn(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(getHeight(newPict)):
      for x in range(0, getWidth(newPict), 2):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict

#Fills every other row and column of a picture with a given color
def colorEveryOther(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(0, getHeight(newPict), 2):
      for x in range(0, getWidth(newPict), 2):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict

#Create plaid effect on a picture with a given color
def colorPlaid(picture, color):
    newPict = duplicatePicture(picture)
    for y in range(0, getHeight(newPict), 4):
      for x in range(getWidth(newPict)):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    for y in range(getHeight(newPict)):
      for x in range(1, getWidth(newPict), 2):
        px = getPixel(newPict, x, y)
        setColor(px, color)
    return newPict

#Draw diagonal line on a square picture with a given color
def diagonalLine(picture, color):
    newPict = duplicatePicture(picture)
    for x in range(getWidth(newPict)):
      px = getPixel(newPict, x, x)
      setColor(px, color)
    return newPict



