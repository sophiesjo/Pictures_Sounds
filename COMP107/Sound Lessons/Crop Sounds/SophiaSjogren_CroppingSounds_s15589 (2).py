#Mini-Lab: Cropping Sounds
#Sophie Sjogren
#5-27-20

#This function crops a given sound starting at a given point and extending to a given number of samples
def cropSound(sound, start, length):
  end = start + length
  soundLength = getNumSamples(sound)
  if(end>=soundLength):
    end = soundLength
  newLength = end-start
  newSound = makeEmptySound(newLength)
  position = 0
  for index in range(start, end):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(newSound, position, value)
    position = position + 1
  return newSound

#This function crops a given sound and uses seconds to start and end cropping
def cropSoundByTime(sound, start, length):
  lengthSound = makeEmptySoundBySeconds(length)
  newLength = getNumSamples(lengthSound)
  startSound = makeEmptySoundBySeconds(start)
  newStart = getNumSamples(startSound)
  newSound = cropSound(sound, newStart, newLength)
  return newSound
    