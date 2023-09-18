#Programming Project: Collage
#Sophie Sjogren
#5-2-20

#This function puts together the collage using the other functions in the program
def collage(width, height, color, firstPic, secondPic, thirdPic, fourthPic, fifthPic):
    canvas = makeEmptyPicture(width, height, color)
    grayedPic = grayScale(firstPic)
    sunsetPic = sunsetEffect(secondPic)
    plaidPic = plaidEffect(thirdPic)
    blurPic = blur(fourthPic)
    posterPic = posterize(fifthPic)
    #Create matte around photos
    for x in range(getWidth(canvas)):
      for y in range(getHeight(canvas)):
        if(x<=10 or x>=(getWidth(canvas)-10)):
          px = getPixel(canvas, x, y)
          setColor(px, darkGray)
        elif(y<=10 or y>=(getHeight(canvas)-10)):
          px = getPixel(canvas, x, y)
          setColor(px, darkGray)
        elif(x>=70 and x<=(getWidth(canvas)-70) and y>=70 and y<=(getHeight(canvas)-70)):
          px = getPixel(canvas, x, y)
          setColor(px, white)
    #Place the first grayed pic in the top left corner
    canvas = copyInto(grayedPic, canvas, 10, 10)
    #Place the first pic not edited slightly over the grayed pic
    canvas = copyInto(firstPic, canvas, 70, 70)
    #Place the second sunset pic in the top right corner
    sunsetX = getWidth(canvas)-getWidth(sunsetPic)-9
    canvas = copyInto(sunsetPic, canvas, sunsetX, 10)
    #Place the second pic not edited over the sunset pic
    canvas = copyInto(secondPic, canvas, sunsetX-60, 70)
    #Place the third plaid pic in the bottom left corner
    plaidY = getHeight(canvas)-getHeight(plaidPic)-9
    canvas = copyInto(plaidPic, canvas, 10, plaidY)
    #Place the third pic not edited over the plaid pic
    canvas = copyInto(thirdPic, canvas, 70, plaidY-60)
    #Place the fourth blur pic in the bottom right corner
    blurX = getWidth(canvas)-getWidth(blurPic)-9
    blurY = getHeight(canvas)-getHeight(blurPic)-9
    canvas = copyInto(blurPic, canvas, blurX, blurY)
    #Place the fourth pic not edited over the blur pic
    canvas = copyInto(fourthPic, canvas, blurX-60, blurY-60)
    #Place the fifth pictures in the middle (posterized version and original blended)
    blendedPic = blendPictures(posterPic, fifthPic, 150)
    blendedX = (getWidth(canvas)/2)-(getWidth(blendedPic)/2)
    blendedY = (getHeight(canvas)/2)-(getHeight(blendedPic)/2)
    canvas = copyInto(blendedPic, canvas, blendedX, blendedY)
    return canvas

#This function copies pictures onto the canvas
def copyInto(origPict, destPict, upperLeftX, upperLeftY):
  if not isinstance(origPict, Picture):
    print "copyInto(origPict, destPict, upperLeftX, upperLeftY): First parameter is not a picture"
    raise ValueError
  if not isinstance(destPict, Picture):
    print "copyInto(origPict, destPict, upperLeftX, upperLeftY): Second parameter is not a picture"
    raise ValueError
  if upperLeftX < 0 or upperLeftX >= getWidth(destPict):
    print "copyInto(origPict, destPict, upperLeftX, upperLeftY): upperLeftX must be within the destPict"
    raise ValueError
  if upperLeftY < 0 or upperLeftY >= getHeight(destPict):
    print "copyInto(origPict, destPict, upperLeftX, upperLeftY): upperLeftY must be within the destPict"
    raise ValueError
  newCanvas = duplicatePicture(destPict)
  origPict.copyInto(newCanvas, upperLeftX, upperLeftY)
  return newCanvas

#This function blends two given images together
def blendPictures(pict1, pict2, overlapAmt):
  width1 = getWidth(pict1)
  height1 = getHeight(pict1)
  width2 = getWidth(pict2)
  height2 = getHeight(pict2)

  # Set up width and height for new canvas
  newWidth = width1 + width2 - overlapAmt
  newHeight = min(height1, height2)

  # Create the canvas to hold the blended pictures
  newCanvas = makeEmptyPicture(newWidth, newHeight)

  # Copy the first picture up to the overlap section
  for x in range(width1 - overlapAmt):
    for y in range(newHeight): 
      color = getColor(getPixel(pict1, x, y))
      setColor(getPixel(newCanvas, x, y), color)

  # Copy the blended section
  # 50% pict1 and 50% pict2
  pict2_x = 0
  for pict1_x in range(width1 - overlapAmt, width1):
    for y in range(newHeight):
      pixel1 = getPixel(pict1, pict1_x, y)
      pixel2 = getPixel(pict2, pict2_x, y)
      newRed = 0.50 * getRed(pixel1) + 0.50 * getRed(pixel2)
      newGreen = 0.50 * getGreen(pixel1) + 0.50 * getGreen(pixel2)
      newBlue = 0.50 * getBlue(pixel1) + 0.50 * getBlue(pixel2)
      color = makeColor(newRed, newGreen, newBlue)
      setColor(getPixel(newCanvas, pict1_x, y), color)
    pict2_x = pict2_x + 1

  # Copy the remaining section of pict2
  targetX = width1
  for x in range(overlapAmt, width2):
    for y in range(newHeight):
      color = getColor(getPixel(pict2, x, y))
      setColor(getPixel(newCanvas, targetX, y), color)
    targetX = targetX + 1

  # Return the new canvas
  return newCanvas

#This function creates a grayscale of a given picture
def grayScale(picture):
    newPict = duplicatePicture(picture)
    for px in getAllPixels(newPict):
      rValue = getRed(px)
      gValue = getGreen(px)
      bValue = getBlue(px)
      intensity = (rValue+gValue+bValue)/3
      newColor = makeColor(intensity, intensity, intensity)
      setColor(px, newColor)
    return newPict

#This function creates a sunset effect of a given picture
def sunsetEffect(picture):
    newPict = duplicatePicture(picture)
    for px in getAllPixels(newPict):
      gValue = getGreen(px)
      bValue = getBlue(px)
      setGreen(px, gValue*0.70)
      setBlue(px, bValue*0.70)
    return newPict

#This function creates a plaid/graph effect on a picture
def plaidEffect(picture):
    newPict = duplicatePicture(picture)
    for y in range(1, getHeight(newPict), 25):
      for x in range(getWidth(newPict)):
        firstpx = getPixel(newPict, x, y)
        secondpx = getPixel(newPict, x, y+1)
        thirdpx = getPixel(newPict, x, y+2)
        setColor(firstpx, black)
        setColor(secondpx, black)
        setColor(thirdpx, black)
    for y in range(0, getHeight(newPict), 25):
      for x in range(getWidth(newPict)):
        firstpx = getPixel(newPict, x, y)
        setColor(firstpx, pink)
    for x in range(1, getWidth(newPict), 25):
      for y in range(getHeight(newPict)):
        firstpx = getPixel(newPict, x, y)
        secondpx = getPixel(newPict, x+1, y)
        thirdpx = getPixel(newPict, x+2, y)
        setColor(firstpx, black)
        setColor(secondpx, black)
        setColor(thirdpx, black) 
    for x in range(0, getWidth(newPict), 25):
      for y in range(getHeight(newPict)):
        firstpx = getPixel(newPict, x, y)
        setColor(firstpx, pink)
    return newPict

#This function blurs a given picture
def blur(pict):
    canvas = makeEmptyPicture(getWidth(pict), getHeight(pict))
    for x in range(1, getWidth(pict)-1):
      for y in range(1, getHeight(pict)-1):
        top = getPixel(pict, x, y-1)
        left = getPixel(pict, x-1, y)
        bottom = getPixel(pict, x, y+1)
        right = getPixel(pict, x+1, y)
        center = getPixel(pict, x, y)
        newRed = (getRed(top)+getRed(left)+getRed(bottom)+getRed(right)+getRed(center))/5
        newGreen = (getGreen(top)+getGreen(left)+getGreen(bottom)+getGreen(right)+getGreen(center))/5
        newBlue = (getBlue(top)+getBlue(left)+getBlue(bottom)+getBlue(right)+getBlue(center))/5
        setColor(getPixel(canvas, x, y), makeColor(newRed, newGreen, newBlue))
    return canvas
 
#This function posterizes a given picture
def posterize(picture):
    newPict = duplicatePicture(picture)
    for px in getAllPixels(newPict):
      redValue = getRed(px)
      blueValue = getBlue(px)
      greenValue = getGreen(px)
      if (redValue < 64):
        setRed(px, 31)
      elif (redValue > 63 and redValue < 128):
        setRed(px, 95)
      elif (redValue > 127 and redValue <192):
        setRed(px, 159)
      else:
        setRed(px, 223)
      if (greenValue < 64):
        setGreen(px, 31)
      elif (greenValue > 63 and greenValue < 128):
        setGreen(px, 95)
      elif (greenValue > 127 and greenValue <192):
        setGreen(px, 159)
      else:
        setGreen(px, 223)
      if (blueValue < 64):
        setBlue(px, 31)
      elif (blueValue > 63 and blueValue < 128):
        setBlue(px, 95)
      elif (blueValue > 127 and blueValue <192):
        setBlue(px, 159)
      else:
        setBlue(px, 223)
    return newPict  

  