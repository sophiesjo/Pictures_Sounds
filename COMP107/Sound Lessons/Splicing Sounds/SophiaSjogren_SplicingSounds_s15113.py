#Lab 6: Splicing Sounds
#Sophie Sjogren
#5-12-20

#This function copies a sound onto a tape at a given starting spot
def copySoundInto(sound, tape, start):
    newSound = duplicateSound(sound)
    newTape = duplicateSound(tape)
    numSamples = getNumSamples(newTape)
    remainingLength = numSamples-start
    soundLength = getNumSamples(newSound)
    if remainingLength <= soundLength:
      endPoint = start+remainingLength
    elif remainingLength >= soundLength:
      endPoint = start+soundLength
    newIndex = 0
    for index in range(start, endPoint):
      value = getSampleValueAt(newSound, newIndex)
      setSampleValueAt(newTape, index, value)
      newIndex = newIndex+1
    return newTape

#This function copies a sound onto a tape at a starting spot given in seconds
def copySoundIntoAtSec(sound, tape, seconds):
    emptySound = makeEmptySoundBySeconds(seconds)
    length = getNumSamples(emptySound)
    finalSound = copySoundInto(sound, tape, length)
    return finalSound
    
#This function reverses a sound
def reverse(sound):
    # create a new empty sound with same # of samples and
    # sampling rate as the original sound
    newSound = makeEmptySound(getNumSamples(sound),int(getSamplingRate(sound)))
    # set up index to start at end of new sound
    newIndex = getNumSamples(newSound) - 1
    # loop through original sound, setting
    # values in new sound
    for index in range(getNumSamples(sound)):
      value = getSampleValueAt(sound, index)
      setSampleValueAt(newSound, newIndex, value)
      newIndex = newIndex - 1

    # return the new sound
    return newSound
    
#This function creates a new sound file that is half of the original given sound and half of that sound in reverse
def forwardAndReverse(sound):
    newSound = duplicateSound(sound)
    reverseSound = reverse(newSound)
    length = getNumSamples(newSound)
    canvas = makeEmptySound(length*2)
    newCanvas = copySoundInto(newSound, canvas, 0)
    newCanvas = copySoundInto(reverseSound, newCanvas, length)
    return newCanvas
