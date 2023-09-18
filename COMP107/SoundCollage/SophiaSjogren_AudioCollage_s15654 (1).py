#Programming Project 3 Audio Collage
#Sophie Sjogren
#5-28-20

#This function uses the given sounds and calls functions throughout the program to return the final sound
def collage(soundOne, soundTwo, soundThree, soundFour):
  sound1 = duplicateSound(soundOne)
  sound2 = duplicateSound(soundTwo)
  sound3 = duplicateSound(soundThree)
  sound4 = duplicateSound(soundFour)
  newSound1 = halfFrequency(sound1)
  newSound2 = echoes(sound2, 10000, 3)
  newSound3 = reverse(sound3)
  newSound4 = decreaseAndIncrease(sound4)
  #to get the length for an empty sound (sorry it's long!)
  length = getNumSamples(sound1)+getNumSamples(newSound1)+getNumSamples(sound2)+getNumSamples(newSound2)+getNumSamples(sound3)+getNumSamples(newSound3)+getNumSamples(sound4)+getNumSamples(newSound4)
  emptySound = makeEmptySound(length)
  collage = copySoundInto(sound1, emptySound, 1)
  collage = copySoundInto(newSound1, collage, getNumSamples(sound1))
  collage = copySoundInto(sound2, collage, getNumSamples(sound1)+getNumSamples(newSound1))
  collage = copySoundInto(newSound2, collage, getNumSamples(sound1)+getNumSamples(newSound1)+getNumSamples(sound2))
  collage = copySoundInto(sound3, collage, getNumSamples(sound1)+getNumSamples(newSound1)+getNumSamples(sound2)+getNumSamples(newSound2))
  collage = copySoundInto(newSound3, collage, getNumSamples(sound1)+getNumSamples(newSound1)+getNumSamples(sound2)+getNumSamples(newSound2)+getNumSamples(sound3))
  collage = copySoundInto(sound4, collage, getNumSamples(sound1)+getNumSamples(newSound1)+getNumSamples(sound2)+getNumSamples(newSound2)+getNumSamples(sound3)+getNumSamples(newSound3))
  collage = copySoundInto(newSound4, collage, getNumSamples(sound1)+getNumSamples(newSound1)+getNumSamples(sound2)+getNumSamples(newSound2)+getNumSamples(sound3)+getNumSamples(newSound3)+getNumSamples(sound4))
  return collage


#This function copies a given sound onto a given tape
def copySoundInto(sound, tape, start):
  newSound = duplicateSound(sound)
  newTape = duplicateSound(tape)
  endPoint = start + getNumSamples(sound)
  newIndex = 0
  for index in range(start, endPoint):
    value = getSampleValueAt(newSound, newIndex)
    setSampleValueAt(newTape, index, value)
    newIndex = newIndex + 1
  return newTape

#This function halves the frequency of a given sound
def halfFrequency(sound):
  numSamples = getNumSamples(sound)
  samplingRate = int(getSamplingRate(sound))
  newSound = makeEmptySound(numSamples * 2, samplingRate)
  index = 0
  for newIndex in range(numSamples * 2):
    val = getSampleValueAt(sound, int(index))
    setSampleValueAt(newSound, newIndex, val)
    index = index + .5 
  return newSound

#This function echos a given sound by a given number of times separated by a given delay time
def echoes(sound, delay, num):
  soundLength = getNumSamples(sound)
  newLength = soundLength + (delay*num) 
  newSound = makeEmptySound(newLength, int(getSamplingRate(sound)))
  echoAmp = 1.0
  for echoCount in range(num+1):
    for soundIndex in range(soundLength):
      newSoundIndex = soundIndex + (delay*echoCount)
      value1 = getSampleValueAt(sound, soundIndex) * echoAmp
      value2 = getSampleValueAt(newSound, newSoundIndex)
      setSampleValueAt(newSound, newSoundIndex, value1+value2)
    echoAmp = echoAmp * .6
  return newSound

#This function reverses a given sound 
def reverse(sound):
  newSound = makeEmptySound(getNumSamples(sound))
  newIndex = getNumSamples(sound) - 1
  for index in range(getNumSamples(sound)):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(newSound, newIndex, value)
    newIndex = newIndex - 1
  return newSound

#This function decreases the first half of a sound file by 70% and increases the second half by 60%
def decreaseAndIncrease(sound):
    newSound = duplicateSound(sound)
    numSamples = getNumSamples(newSound)
    for index in range(numSamples/2):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 0.30)
    for index in range(numSamples/2, numSamples):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 1.60)
    return newSound


