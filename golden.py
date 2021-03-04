import cv2
from skimage import io
import math
import numpy as np

img = io.imread(
    "https://fessenden.myschoolapp.com/ftpimages/7/user/large_user_5031860_61.jpg?resize=200,200")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

def slope_diff(one, two, three):
  slope1 = (two[1] - one[1]) / (two[0] - one[0])
  slope2 = (three[1] - two[1]) / (three[0] - two[0])

  inc1 = math.radians(math.atan(slope1))
  inc2 = math.radians(math.atan(slope2))

  return 180 - abs(inc2 - inc1)

found = []

def check_found(new, found):
    for i in found:
        if set(new) == set(i):
            return True

    return False


for i in range(len(corners)):
    for j in range(len(corners)):
        if j == i:
            continue
        for k in range(len(corners)):
            if k == j or k == i:
                continue
            diff = slope_diff(corners[i][0], corners[j][0], corners[k][0])
            print(diff)
            ratio = round(math.dist(corners[i][0], corners[j][0]) / math.dist(corners[j][0], corners[k][0]), 2)
            if ratio >= 1.60 and ratio <= 1.62 and diff >= 0 and diff <= .2:
                if not check_found([i, j, k], found):
                    print(diff)
                    img = cv2.line(img, tuple(corners[i][0]), tuple(
                        corners[j][0]), (0, 0, 225), 1)
                    img = cv2.line(img, tuple(corners[j][0]), tuple(
                        corners[k][0]), (255, 0, 0), 1)
                    found.append([i, j, k])

cv2.imwrite("test.png", img)