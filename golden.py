import cv2
from skimage import io
import math
import numpy as np

img = io.imread(
    "https://farm1.static.flickr.com/161/438778468_4e7c6f5677.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)


def slope_diff(one, two, three, y):
    slope1 = ((y - two[1]) - (y - one[1])) / (two[0] - one[0])
    slope2 = ((y - three[1]) - (y - two[1])) / (three[0] - two[0])

    return abs(slope2 - slope1)


found = []


def check_found(new, found):
    for i in found:
        if set(new) == set(i):
            return True

    return False


y, _, _ = img.shape

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
                diff = slope_diff(
                    corners[i][0], corners[j][0], corners[k][0], y)
                direction = math.dist(
                    corners[i][0], corners[k][0]) - math.dist(corners[i][0], corners[j][0])
                if ratio >= 1.57 and ratio <= 1.64 and diff >= 0 and diff <= .4 and direction > 0:
                    img = cv2.line(img, tuple(corners[i][0]), tuple(
                        corners[j][0]), (0, 0, 225), 10)
                    img = cv2.line(img, tuple(corners[j][0]), tuple(
                        corners[k][0]), (255, 0, 0), 10)
                    found.append([i, j, k])

cv2.imwrite("test.png", img)
