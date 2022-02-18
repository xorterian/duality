# Run Cmd as admin, e.g.: C:\Python386\python.exe C:\Users\Kristóf\Desktop\Munka\Referencia\Image\IxI2I-Dualize.py "C:\Users\Kristóf\Desktop\Munka\Referencia\Image\image1.bmp" "C:\Users\Kristóf\Desktop\Munka\Referencia\Image\image2.bmp" "C:\Users\Kristóf\Desktop\Munka\Referencia\Image\result.bmp"
import numpy as np
import cv2
import math
import optparse
from PIL import Image, ImageSequence
from LogFun import *

parser = optparse.OptionParser(usage = 'usage: %prog [function of (x,y)] [size: width, height] [output filename]')
options, args = parser.parse_args()
Ima1, Ima2, Res = Image.open(args[0]), Image.open(args[1]), args[2]
Ima1, Ima2 = np.asarray(Ima1), np.asarray(Ima2)

dx, dy, dz = Ima1.shape
ima = np.zeros((dx,dy,dz)).astype(np.uint8)
for x in range(dx):
 for y in range(dy):
  for z in range(dz):
   ima[x,y,z] = (Ima1[x,y,z]//16)*16 + rev(Ima2[x,y,z]//16,4)

ima = Image.fromarray(ima)
ima.save(Res)
ima.show()

cv2.waitKey(0)
cv2.destroyAllWindows()