# Run Cmd as admin, e.g.: 
# C:\Python386\python.exe C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Trigital\S3S-Depth-Rev.py "C:\Users\Kristóf\Desktop\Munka\Referencia\Result.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\Result-trial.wav"
from LogFun import *
import numpy as np
import math
from scipy.io.wavfile import write
import wave
import optparse

# inputs from terminal
parser = optparse.OptionParser(usage = 'usage: %prog [function of t] [length (ms)] [output filename]')
options, args = parser.parse_args()
FNameIn,FNameOut = args[0],args[1]

fs = 44100

# reading wav sounds
def readM(name):
    music = wave.open(name)
    samples = music.getnframes()
    audio = music.readframes(samples)
    audio = np.frombuffer(audio, dtype=np.int16)
    return audio

# changing the length of an audio vector
def speeder(u,rate):
    return [ u[math.floor(t*rate)%len(u)] for t in range(math.floor(len(u)/rate)) ]

# permutation product
def pprod(u,v):
  return [u[i-1] for i in v]
# a permutation cube-root of the 15-long identity permutation
u=[8, 7, 10, 9, 6, 13, 12, 15, 14, 11, 3, 2, 5, 4, 1]

# E.g. make_trial(23000,6666,9023) = 22632
# Then 22632 is approximately 23k, its first trial: trial(22632) is 6419 is approximately 6666, and the second trial: trial(trial(22632)) is 8434 is approximately 9023 - more or less.
# Ofc, it satisfies the triality property: trial(trial(trial(x))) = x for each int between 1 and 2**15.
def trial(x):
  return sum([ int(pprod(('{:15b}').format(x).replace(' ','0')[:15],u)[i])*2**(14-i) for i in range(15) ])

print('Reading...')
snd = readM(FNameIn).astype(np.uint16)
print('Trializing...')
snd = np.array([ trial(math.floor(snd[t])) for t in range(len(snd))])
print('Saving...')
write(FNameOut,fs*2,snd.astype(np.int16))
