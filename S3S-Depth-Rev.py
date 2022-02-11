# Run Cmd as admin, e.g.: 
# C:\Python386\python.exe C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Trigital\S3S-Depth-Rev.py "C:\Users\Kristóf\Desktop\Munka\Referencia\Result.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\Result-trial.wav"
from LogFun import *
import numpy as np
import math
from scipy.io.wavfile import write
import wave
import optparse

parser = optparse.OptionParser(usage = 'usage: %prog [function of t] [length (ms)] [output filename]')
options, args = parser.parse_args()
FNameIn,FNameOut = args[0],args[1]
fs = 44100

def readM(name):
    music = wave.open(name)
    samples = music.getnframes()
    audio = music.readframes(samples)
    audio = np.frombuffer(audio, dtype=np.int16)
    return audio

def speeder(u,rate):
    return [ u[math.floor(t*rate)%len(u)] for t in range(math.floor(len(u)/rate)) ]

def pprod(u,v):
  return [u[i-1] for i in v]
u=[8, 7, 10, 9, 6, 13, 12, 15, 14, 11, 3, 2, 5, 4, 1]

def trial(x):
  return sum([ int(pprod(('{:15b}').format(x).replace(' ','0')[:15],u)[i])*2**(14-i) for i in range(15) ])

print('Reading...')
snd = readM(FNameIn).astype(np.uint16)
print('min: ',np.min(snd))
print('max: ',np.max(snd))
print('Trializing...')
snd = np.array([ trial(math.floor(snd[t])) for t in range(len(snd))])
print('Saving...')
write(FNameOut,fs*2,snd.astype(np.int16))
