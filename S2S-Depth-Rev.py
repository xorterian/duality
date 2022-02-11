# Run Cmd as admin, e.g.: 
# C:\Python386\python.exe C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Depth-Rev.py "C:\Users\Kristóf\Desktop\Munka\Referencia\Source.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\Result.wav"
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

print('Reading...')
snd = readM(FNameIn).astype(np.uint16)
print('min: ',np.min(snd))
print('max: ',np.max(snd))
print('Reversing...')
snd = np.array([ rev(math.floor(snd[t]),16) for t in range(len(snd))])
print('Saving...')
write(FNameOut,fs*2,snd.astype(np.int16))
