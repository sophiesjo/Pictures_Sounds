#Mini-Lab: Changing Volume
#Sophie Sjogren
#5-8-20

#This function increases or decreases the volume of a given sound by a given factor
def changeVolume(sound, factor):
    newSound = duplicateSound(sound)
    for sample in getSamples(newSound):
      value = getSampleValue(sample)
      setSampleValue(sample, value*factor)
    return newSound

#This function increases the first half of the sound file by doubling it and decreases the second half by 40%
def increaseAndDecrease(sound):
    newSound = duplicateSound(sound)
    numSamples = getNumSamples(newSound)
    for index in range(numSamples/2):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 2)
    for index in range(numSamples/2, numSamples):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 0.60)
    return newSound
    
#This function decreases the first half of a sound file by 50% and increases the second half by 50%
def decreaseAndIncrease(sound):
    newSound = duplicateSound(sound)
    numSamples = getNumSamples(newSound)
    for index in range(numSamples/2):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 0.50)
    for index in range(numSamples/2, numSamples):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 1.50)
    return newSound

#This function gradual decreases the volume of a sound file. First third by 30%, then 60%, then 90%
def gradualDecrease(sound):
    newSound = duplicateSound(sound)
    numSamples = getNumSamples(newSound)
    for index in range(numSamples/3):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 0.70)
    for index in range(numSamples/3, (numSamples*2)/3):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 0.40)
    for index in range((numSamples*2)/3, numSamples):
      value = getSampleValueAt(newSound, index)
      setSampleValueAt(newSound, index, value * 0.10)
    return newSound
    
#This function makes the volume of the file as loud as possible    
def normalize(sound):
    newSound = duplicateSound(sound)
    largest = 0
    for s in getSamples(newSound):
      largest = max(largest, abs(getSampleValue(s)))
    factor = 32767.0/largest
    for s in getSamples(newSound):
      value = getSampleValue(s)
      setSampleValue(s, value * factor)
    return newSound
    