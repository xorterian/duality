# Run Cmd as admin, e.g.: C:\Python386\python.exe C:\Users\Kristóf\Desktop\Munka\Referencia\Image\I2I-Depth-Rev.py "C:\Users\Kristóf\Desktop\Munka\Referencia\Image\result.bmp" "C:\Users\Kristóf\Desktop\Munka\Referencia\Image\result-rev.bmp"
import numpy as np
import cv2
import math
import optparse
from PIL import Image, ImageSequence
from LogFun import *

parser = optparse.OptionParser(usage = 'usage: %prog [function of (x,y)] [size: width, height] [output filename]')
options, args = parser.parse_args()
Ima, Res = Image.open(args[0]), args[1]
Ima = np.asarray(Ima)

dx, dy, dz = Ima.shape
ima = np.zeros((dx,dy,dz)).astype(np.uint8)
for x in range(dx):
 for y in range(dy):
  for z in range(dz):
   ima[x,y,z] = rev(Ima[x,y,z])

ima = Image.fromarray(ima)
ima.save(Res)
ima.show()

cv2.waitKey(0)
cv2.destroyAllWindows()