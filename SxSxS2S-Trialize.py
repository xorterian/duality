# Run Cmd as admin, e.g.: 
# C:\Python386\python.exe C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Trigital\SxSxS2S-Trialize.py "C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Trigital\trim-1.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Trigital\trim-2.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Trigital\trim-3.wav" "C:\Users\Kristóf\Desktop\Munka\Referencia\S2S-Trigital\Result.wav"
from LogFun import *
import numpy as np
import math
from scipy.io.wavfile import write
import wave
import optparse

# inputs from terminal
parser = optparse.OptionParser(usage = 'usage: %prog [function of t] [length (ms)] [output filename]')
options, args = parser.parse_args()
FName1,FName2,FName3,FNameOut = args[0],args[1],args[2],args[3]

fs = 44100

# reading a wav file
def readM(name):
    music = wave.open(name)
    samples = music.getnframes()
    audio = music.readframes(samples)
    audio = np.frombuffer(audio, dtype=np.int16)
    return audio

# changing the length of the audio file
def speeder(u,rate):
    return [ u[math.floor(t*rate)%len(u)] for t in range(math.floor(len(u)/rate)) ]

# permutation product
def pprod(u,v):
  return [u[i-1] for i in v]
# a permutation cube-root of the 5-long identity permutation vector
p=[3, 2, 5, 4, 1]

# it makes three 15-bit ints a so-called triality number whose trials approach the input numbers
# E.g. make_trial(23000,6666,9023) = 22632
# 22632 is approximately 23k, its first trial is 6419 is approximately 6666, and the second trial is 8434 is approximately 9023 - more or less.
def make_trial(a,b,c):
  a,b,c = a//1024,b//1024,c//1024
  b = sum([ int(pprod(('{:5b}').format(b).replace(' ','0')[:5],pprod(p,p))[i])*2**(4-i) for i in range(5) ])
  c = sum([ int(pprod(('{:5b}').format(c).replace(' ','0')[:5],p)[i])*2**(4-i) for i in range(5) ])
  return a*2**10+b*2**5+c

# Reading inputs...
input1, input2, input3 = readM(FName1).astype(np.uint16)//2, readM(FName2).astype(np.uint16)//2, readM(FName3).astype(np.uint16)//2

# Making lengths of the inputs the same
L=max(len(input1),max(len(input2),len(input3)))
print('Length: ',L)
if len(input1)==L:
  input2=speeder(input2,len(input2)/L)
  input3=speeder(input3,len(input3)/L)
elif len(input2)==L:
  input1=speeder(input1,len(input1)/L)
  input3=speeder(input3,len(input3)/L)
else:
  input1=speeder(input1,len(input1)/L)
  input2=speeder(input2,len(input2)/L)

print('Making trial...')
snd = np.array([ make_trial(input1[t],input2[t],input3[t]) for t in range(L)]).astype(np.int16)

print('Saving...')
write(FNameOut,fs*2,snd)
