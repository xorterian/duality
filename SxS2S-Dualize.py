# Run Cmd as admin, e.g.: 
# C:\Python386\python.exe C:\Users\Kristóf\Desktop\Munka\Referencia\SxS2S-Dualize.py "C:\Users\Kristóf\Desktop\Munka\Referencia\Dual-U.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\Dual-D.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\Result.wav"
from LogFun import *
import numpy as np
import math
from scipy.io.wavfile import write
import wave
import optparse

parser = optparse.OptionParser(usage = 'usage: %prog [function of t] [length (ms)] [output filename]')
options, args = parser.parse_args()
#print("options: ",options)
print("args: ",args)
FName1,FName2,FNameOut = args[0],args[1],args[2]
fs = 44100

def readM(name):
    music = wave.open(name)
    samples = music.getnframes()
    audio = music.readframes(samples)
    audio = np.frombuffer(audio, dtype=np.int16)#.astype(np.float32) / 2 ** 15
    return audio

def speeder(u,rate):
    return [ u[math.floor(t*rate)%len(u)] for t in range(math.floor(len(u)/rate)) ]

# Reading inputs...
input1, input2 = readM(FName1).astype(np.uint16)//2**8, readM(FName2).astype(np.uint16)//2**8

# Making lengths of the inputs the same
L=max(len(input1),len(input2))
print('Length: ',L)
if len(input1)==L:
  input2=speeder(input2,len(input2)/L)
else:
  input1=speeder(input1,len(input1)/L)
print('max_in1: ',np.max(input1))
print('max_in2: ',np.max(input2))

print('Making dual...')
snd = np.array([input1[t]*2**8+rev(input2[t]) for t in range(L)]).astype(np.int16)
print('max_out: ',np.max(snd))

print('Saving...')
write(FNameOut,fs*2,snd)