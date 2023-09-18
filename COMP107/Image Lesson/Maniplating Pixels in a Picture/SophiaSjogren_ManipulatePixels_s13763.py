#Mini-Lab: Functions that Manipulate Pixels in a Picture
#Sophie Sjogren
#4-10-20

#To reduce the amount of red in a picture by 25%
def reduceRed(pict):
    newPict = duplicatePicture(pict)
    for px in getAllPixels(newPict):
      value = getRed(px)
      setRed(px, value*0.75)
    return newPict
    
#To increase the amount of red in a picture by 30%
def increaseRed(pict):
    newPict = duplicatePicture(pict)
    for px in getAllPixels(newPict):
      value = getRed(px)
      setRed(px, value*1.30)
    return newPict
#The two functions, reduceRed and increaseRed, are very similar and are set up the same way with the for loop and the steps used to set the red value in a pixel. The only difference is the number multiplied by the value in the setRed function. To reduce the red value, the program uses a number value less than 1, but to increase the red value, the program uses a number greater than 1.

#To set the blue and green values equal to the red value of each pixel in a picture
def showRedChannel(pict):
    newPict = duplicatePicture(pict)
    for px in getAllPixels(newPict):
       value = getRed(px)
       newColor = makeColor(value, value, value)
       setColor(px, newColor)
    return newPict
#The showRedChannel changes a colorful image into a black and white image which highlights the red areas. In a region that was initially red, the region is now black or gray. In a region that was initially blue, the region is now white.

#To create the sunset effect in a picture
def makeSunset(pict):
    newPict = duplicatePicture(pict)
    for px in getAllPixels(newPict):
      gvalue = getGreen(px)
      bvalue = getBlue(px)
      setGreen(px, gvalue*0.70)
      setBlue(px, bvalue*0.70)
    return newPict