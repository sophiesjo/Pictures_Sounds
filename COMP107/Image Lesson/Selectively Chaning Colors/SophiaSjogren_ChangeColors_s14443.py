#Mini-Lab: Selectively Changing Colors
#Sophie Sjogren
#4-24-20

#This function replaces one color in an image with another color
def colorSwitch( pic, origColor, newColor):
    newPict = duplicatePicture(pic)
    for px in getAllPixels(newPict):
      if(distance(origColor, getColor(px))<200):
        setColor(px, newColor)
    return newPict

#The function could be used to remove red-eye if the only red in the picture is in the eye, but most likely a change would be necessary. To change the function, you would need to use the range function in order to read the pixels in a specific region of the picture. 
