#Lab 4: Combining Pictures
#Sophie Sjogren
#4-26-20

#This function swaps the background when a picture of someone (pict) and a picture of where they stood without them (bg) is given and the background is changed to be a new background (newBg) 
def swapBack(pict, bg, newBg):
    newPict = duplicatePicture(pict)
    for y in range(getHeight(newPict)):
      for x in range(getWidth(newPict)):
        px1 = getPixel(newPict, x, y)
        bgpx = getPixel(bg, x, y)
        if (distance(getColor(px1), getColor(bgpx)) < 100.0):
          setColor(px1, getColor(getPixel(newBg, x, y)))
    return newPict
 
#This function takes a green screen picture (pict) and changes the background to a given picture (bg)
def chromakey(pict, bg):
    newPict = duplicatePicture(pict)
    for y in range(getHeight(newPict)):
      for x in range(getWidth(newPict)):
        px = getPixel(newPict, x, y)
        # A definition of green
        if (getRed(px) < 175 and getRed(px) > 75 and getBlue(px) < 175 and getBlue(px) > 75):
          # then grab the color at the same spot from the bg
          setColor(px, getColor(getPixel(bg, x, y)))
    return newPict

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