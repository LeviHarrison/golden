import cv2
from skimage import io
import math
import numpy as np

img = io.imread("https://fessenden.myschoolapp.com/ftpimages/7/user/large_user_5031860_61.jpg?resize=200,200")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in range(len(corners)):
  for j in range(len(corners)):
    if j == i:
      continue
    for k in range(len(corners)):
      if k == j or k == i:
        continue

      if round(math.dist(corners[i][0], corners[j][0]) / math.dist(corners[j][0], corners[k][0]), 1) == 1.6:
        x,y = corners[i].ravel()
        cv2.circle(img,(x,y),3,255,-1)
        x,y = corners[j].ravel()
        cv2.circle(img,(x,y),3,255,-1)
        x,y = corners[k].ravel()
        cv2.circle(img,(x,y),3,255,-1)

cv2.imwrite("test.png", img)
