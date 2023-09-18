#Lab: Simple Picture Manipulation
#Sophie Sjogren
#4-12-20

#This function adjusts the amount of red in the given picture according to the given multiplier. The given multiplier is a numerical value that would increase or decrease the red value. For example: if the program was given 1.2, it would increase the value by %20. Vice versa to decrease the value by %20, the entered multiplier would be 0.8.
def adjustRed(picture, multiplier):            #make sure picture is a file made into a picture and the multiplier is a number. 
    newPict = duplicatePicture(picture)
    
    for px in getAllPixels(newPict):
      value = getRed(px)
      setRed(px, value*multiplier)
    return newPict
#For the function name, "adjustRed" fits the action of changing the red value, but does not specify increase or decrease. Multiplier is a good name for the new parameter because it is the number being multiplied by the red value, so "multiplier".

#This function adjusts the amount of green in the given picture according to the given multiplier. The given multiplier is a numerical value that would increase or decrease the green value. For example: if the program was given 1.2, it would increase the value by %20. Vice versa to decrease the value by %20, the entered multiplier would be 0.8.
def adjustGreen(picture, multiplier):            #make sure picture is a file made into a picture and the multiplier is a number. 
    newPict = duplicatePicture(picture)
    
    for px in getAllPixels(newPict):
      value = getGreen(px)
      setGreen(px, value*multiplier)
    return newPict

#This function adjusts the amount of blue in the given picture according to the given multiplier. The given multiplier is a numerical value that would increase or decrease the blue value. For example: if the program was given 1.2, it would increase the value by %20. Vice versa to decrease the value by %20, the entered multiplier would be 0.8.
def adjustBlue(picture, multiplier):            #make sure picture is a file made into a picture and the multiplier is a number. 
    newPict = duplicatePicture(picture)
    
    for px in getAllPixels(newPict):
      value = getBlue(px)
      setBlue(px, value*multiplier)
    return newPict

#This function adds a sunset effect to a given picture by calling on other functions
def makeSunset(picture):
    #it is not necessary to duplicate the image because the adjustGreen and adjustBlue functions create the duplicate 
    #adjust the green value 
    lessGreen = adjustGreen(picture, 0.70)
    show(lessGreen)
    
    #adjust the blue value
    lessBlue = adjustBlue(lessGreen, 0.70)
    show(lessBlue)
    
    return lessBlue

#This function creates a negative copy of a given picture
def negative(picture):
    newPict = duplicatePicture(picture)

    for px in getAllPixels(newPict):
      rvalue = getRed(px)
      gvalue = getGreen(px)
      bvalue = getBlue(px)
      negColor = makeColor(255-rvalue, 255-gvalue, 255-bvalue)
      setColor(px, negColor)

    return newPict
 
#This function creates a gray scale copy of a given picture
def grayscale(picture):
    newPict = duplicatePicture(picture)
    
    for px in getAllPixels(newPict):
      rvalue = getRed(px)
      gvalue = getGreen(px)
      bvalue = getBlue(px)
      intensity = (rvalue + gvalue + bvalue)/3
      newColor = makeColor(intensity, intensity, intensity)
      setColor(px, newColor)

    return newPict
    
#This function creates a weighted gray scale copy of a given picture
def weightedGrayScale(picture):
    newPict = duplicatePicture(picture)

    for px in getAllPixels(newPict):
      newRValue = getRed(px) * 0.299
      newGValue = getGreen(px) * 0.587
      newBValue = getBlue(px) * 0.114
      luminance = newRValue + newGValue + newBValue
      newColor = makeColor(luminance, luminance, luminance)
      setColor(px, newColor)

    return newPict

#This function makes a nature picture taken in summer appear to have been taken in fall with not so green plants
def makeFall(picture):
    newPict = duplicatePicture(picture)
    
    for px in getAllPixels(newPict):
      rvalue = getRed(px)
      bvalue = getBlue(px)
      newGreen = (rvalue+bvalue)/2.0
      newColor = makeColor(rvalue, newGreen, bvalue)
      setColor(px, newColor)
      
    return newPict
