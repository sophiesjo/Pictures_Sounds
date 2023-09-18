#Mini-Lab: Changing Frequency
#Sophie Sjogren
#5-11-20

# This function halves the frequency of the original sound
# The new sound is twice as long, and sounds slower and deeper
def halfFrequency(sound):
    # make a new sound with twice as many samples and same
    # sampling rate as original sound
    numSamples = getNumSamples(sound)
    samplingRate = int(getSamplingRate(sound))
    newSound = makeEmptySound(numSamples * 2, samplingRate)

    # Use a loop to get values from original sound, setting values in new sound
    index = 0
    for newIndex in range(numSamples * 2):
      val = getSampleValueAt(sound, int(index))
      setSampleValueAt(newSound, newIndex, val)
      index = index + .5   # Allows us to use each original sample twice
    
    # return the new sound
    return newSound

# This function doubles the frequency of the original sound
# The new sound is half as long, and sounds quicker and higher-pitched
def doubleFrequency(sound):
    numSamples = getNumSamples(sound)
    samplingRate = int(getSamplingRate(sound))
    newSound = makeEmptySound(numSamples/2, samplingRate)  

    index = 0
    for newIndex in range(numSamples/2):
      val = getSampleValueAt(sound, int(index))
      setSampleValueAt(newSound, newIndex, val)
      index = index + 2
    return newSound