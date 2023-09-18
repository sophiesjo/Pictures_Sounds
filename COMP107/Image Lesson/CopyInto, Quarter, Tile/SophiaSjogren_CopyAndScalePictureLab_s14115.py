#Lab: Copying a Picture Into a Bigger Picture and Scaling Pictures
#Sophie Sjogren
#4-19-20

#This function copies a picture onto another canvas
def copyInto(picture, canvas, upperLeftX, upperLeftY):
  #duplicate the canvas     
  newCanvas = duplicatePicture(canvas)
  #get the widths and heights
  pictureWidth = getWidth(picture)
  pictureHeight = getHeight(picture)
  canvasWidth = getWidth(newCanvas)
  canvasHeight = getHeight(newCanvas)
  #find width and height to trim inside picture to fit size
  widthToCopy = min(pictureWidth, canvasWidth-upperLeftX)
  heightToCopy = min(pictureHeight, canvasHeight-upperLeftY)
  #copy and add the picture
  targetX = upperLeftX
  for sourceX in range(widthToCopy):
    targetY = upperLeftY
    for sourceY in range(heightToCopy):
      sourcePix = getPixel(picture, sourceX, sourceY)
      color = getColor(sourcePix)
      destPix = getPixel(newCanvas, targetX, targetY)
      setColor(destPix, color)
      targetY = targetY + 1
    targetX = targetX +1
  return newCanvas
#The function allows the canvas to be either a blank canvas or a copy of a picture

#To create a black matte surrounding a given picture
def matte(picture, matteWidth):
    #dupliate original picture
    newPic = duplicatePicture(picture)
    #get the height and width and added space in a row or column
    picHeight = getHeight(newPic)
    picWidth = getWidth(newPic)
    addedSpace = matteWidth*2
    #create the new canvas and use the copyOnto function to create the new picture
    canvas = makeEmptyPicture(picWidth+addedSpace, picHeight+addedSpace, black)
    pic = copyInto(newPic, canvas, matteWidth, matteWidth)
    return pic
    
#To create a two layer matte around a given picture with black and a given color. The smaller matte is automatically 10 pixels, but the larger matte is a given length.
def twoMatte(picture, matteWidth, color):
    #duplicate original picture
    newPic = duplicatePicture(picture)
    #get the height and width of picture
    picHeight = getHeight(newPic)
    picWidth = getWidth(newPic)
    #create the first matte by making the canvas and using the copyOnto function
    firstCanvas = makeEmptyPicture(picWidth+20, picHeight+20, color)
    firstPic = copyOnto(newPic, firstCanvas, 10, 10)
    #create the second matte by making the blakc canvas and using the copyOnto function again
    addedSpace = matteWidth*2
    secondCanvas = makeEmptyPicture(getWidth(firstPic)+addedSpace, getHeight(firstPic)+addedSpace, black)
    secondPic = copyInto(firstPic, secondCanvas, matteWidth, matteWidth)
    return secondPic
    
# This function returns a new picture 1/4 the size of the original picture
def quarter(orig):
    #get the original width and height and divide them in half
    newWidth = getWidth(orig)/2
    newHeight = getHeight(orig)/2
    #make an empty picture to store the scaled image
    newCanvas = makeEmptyPicture(newWidth,newHeight)
    #copy every other pixel onto the new canvas
    for targetX in range(newWidth):
      for targetY in range(newHeight):
        color = getColor(getPixel(orig, targetX*2, targetY*2))
        setColor(getPixel(newCanvas, targetX, targetY), color)
    return newCanvas

# Fills a canvas with as many copies of a picture as will fit, including partial copies of the picture along the right and lower edges if necessary
def tile(picture, canvas):
    for targetY in range(0, getHeight(canvas),getHeight(picture)):
      for targetX in range(0, getWidth(canvas), getWidth(picture)):
        canvas = copyInto(picture, canvas, targetX, targetY)
    return canvas
  
#This function takes a picture and makes quarters of the picture and tiles the original image with the quarter pictures
def tileWithQuarters(orig):
    newPic = duplicatePicture(orig)
    smallPic = quarter(newPic)
    finalPic = tile(smallPic, orig)
    return finalPic