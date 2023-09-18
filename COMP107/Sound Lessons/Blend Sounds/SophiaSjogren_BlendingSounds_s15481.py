#Mini-Lab: Blending Sounds
#Sophie Sjogren
#5-22-20

# Blend sound1 with sound2
# return the resulting sound
def blendSounds(sound1, sound2):
  if getSamplingRate(sound1) != getSamplingRate(sound2):
    print "Error! Sounds must have the same sampling rate."
    return

  # Determine which sound has minimum length
  minimum = min(getNumSamples(sound1), getNumSamples(sound2))
  newList = [0]*minimum
  # Create a new sound of that length
  newSound = makeEmptySound(minimum)
  for index in range(minimum):
    # Get the appropriate sample values from each sound
    val1 = getSampleValueAt(sound1, index)
    val2 = getSampleValueAt(sound2, index)
    # Add the sample values together
    newVal = val1 + val2
    setSampleValueAt(newSound, index, newVal)
  return newSound
    
#-----------------------------
#Takes a python list of numbers, and a sampling rate
#and returns a sound object. 
#-----------------------------
def listToSound(list, samplingRate):
  newSound = makeEmptySound(len(list), int(samplingRate))
  for pos in range(getNumSamples(newSound)):
    setSampleValueAt(newSound, pos, list[pos])
  return newSound

#-----------------------------
#Normalizes a list of numbers so that the maximum value
#in the list will be newMax. 
#THIS FUNCTION DOES NOT RETURN ANYTHING. IT CHANGES THE 
#LIST THAT IS PASSED IN AS A PARAMETER. 
#-----------------------------
def normalizeList(list, newMax):
  oldMax = max(list)
  for pos in range(len(list)):
    list[pos] = list[pos] * newMax/oldMax


#-----------------------------
#Blend two sounds together, rescaling the resulting sound if necessary 
#to avoid clipping. 
#-----------------------------
def blendSoundsNoClipping(sound1, sound2):
  if getSamplingRate(sound1) != getSamplingRate(sound2):
    print "Error! Sounds must have the same sampling rate."
    return

  minLength = min(getNumSamples(sound1), getNumSamples(sound2))
  newSoundList = [0.0] * minLength 

  #Now add the sample values of the two sounds together, 
  #placing the result in newSoundList
  for pos in range(minLength):
     #ADD CODE BELOW TO SUM UP THE CORRESPONDING SAMPLE VALUES
     val1 = getSampleValueAt(sound1, pos)
     val2 = getSampleValueAt(sound2, pos)
     newSoundList[pos] = val1 + val2

  maxVal = max(newSoundList) #calculate the maximum sample value

  #ADD CODE TO COMPLETE THE FOLLOWING THREE STEPS...
  #If maxVal> 32767, there has been clipping, normalize the sound.
  if(maxVal > 32767):
    normalize(newSoundList)
  #Use listToSound to create the final sound from newSoundList.
  samplingRate = getSamplingRate(sound1)
  finalSound = listToSound(newSoundList, samplingRate)
  #Return the resulting sound.
  return finalSound
