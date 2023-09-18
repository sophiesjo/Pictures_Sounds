#Mini-Lab: Reflecting Pictures
#Sophie Sjogren
#4-17-20

#Reflects the given picture vertically
def verticalReflection(picture):
    #Get the width and height of original picture
    width = getWidth(picture)
    height = getHeight(picture)
    #Create a new picture
    pic = makeEmptyPicture(width, height, white)
    #Create loop function for every row then every column
    for y in range(height):
      for x in range(width):
        #Get the color values from the original picture
        px = getPixel(picture, x, y)
        r = getRed(px)
        g = getGreen(px)
        b = getBlue(px)
        #Assign those color values to the new picture, but with opposite x values
        newPx = getPixel(pic, width-x-1, y)
        setRed(newPx, r) 
        setGreen(newPx, g)
        setBlue(newPx, b)
    return pic
#When reflecting vertically, the y coordinate will remain the same, but the x vaue will become the width minus the original x value
    