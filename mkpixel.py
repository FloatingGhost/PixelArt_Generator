#!/usr/bin/env python3

from PIL import Image
import sys


toBlend = int(sys.argv[1])

def doTheRoar(f, blend):
  print("Pixel-ising {}".format(f))
  im = Image.open(f)
  px = im.load()
  print(px)
  width = im.width
  height = im.height
  
  if height / blend != height // blend:
    print("Blend value not a divisor of height, continuing...")

  if width / blend != width // blend:
    print("Blend value is not a divisor of width, continuing...")

  
  for i in range(0, width, blend):
    for j in range(0, height, blend):
      dicty = {}
      try:
        for k in range(blend):
          for l in range(blend):
            if px[i+k,j+l] in dicty:
              dicty[px[i+k,j+l]] += 1
            else:
              dicty.update({px[i+k,j+l]:1})
        for k in range(blend):
          for l in range(blend):
            px[i+k,j+l] = max(dicty)
      except Exception:
        break
  im.save(f + ".PIX", "PNG")
  im.close()  
  print("Saved {}.PIX".format(f)) 

for i in sys.argv[2:]:
  doTheRoar(i, toBlend)
