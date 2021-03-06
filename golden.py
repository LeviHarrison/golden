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
    slope1 = ((200 - two[1]) - (200 - one[1])) / (two[0] - one[0])
    slope2 = ((200 - three[1]) - (200 - two[1])) / (three[0] - two[0])

    return abs(slope2 - slope1)


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
            if not check_found([i, j, k], found):
                ratio = round(math.dist(
                    corners[i][0], corners[j][0]) / math.dist(corners[j][0], corners[k][0]), 2)
                diff = slope_diff(corners[i][0], corners[j][0], corners[k][0])
                direction = math.dist(
                    corners[i][0], corners[k][0]) - math.dist(corners[i][0], corners[j][0])
<<<<<<< HEAD
                if ratio >= 1.59 and ratio <= 1.63 and diff >= 0 and diff <= .4 and direction > 0:
=======
                if ratio >= 1.60 and ratio <= 1.62 and diff >= 0 and diff <= .4 and direction > 0:
>>>>>>> parent of 3ce6f16... Changed un-cving of y axis
                    img = cv2.line(img, tuple(corners[i][0]), tuple(
                        corners[j][0]), (0, 0, 225), 1)
                    img = cv2.line(img, tuple(corners[j][0]), tuple(
                        corners[k][0]), (255, 0, 0), 1)
                    found.append([i, j, k])

cv2.imwrite("test.png", img)
