import cv2
from skimage import io
import math
import numpy as np
import requests
import sqlite3


def check_found(new, found):
    for i in found:
        if set(new) == set(i):
            return True

    return False


def slope_diff(one, two, three):
    slope1 = ((200 - two[1]) - (200 - one[1])) / (two[0] - one[0])
    slope2 = ((200 - three[1]) - (200 - two[1])) / (three[0] - two[0])

    return abs(slope2 - slope1)


banned = ["opium", "marijuana", "pot", "cocain", "poppy", "poppies"]

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()

table = """
CREATE TABLE IF NOT EXISTS golden (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    catagory TEXT NOT NULL,
    x1 INTEGER NOT NULL,
    y1 INTEGER NOT NULL,
    x2 INTEGER NOT NULL,
    y2 INTEGER NOT NULL,
    x3 INTEGER NOT NULL,
    y3 INTEGER NOT NULL
);
"""
cur.execute(table)
conn.commit()

while True:
    data = requests.get("http://localhost:8080/job").json()

    try:
        img = io.imread(data["url"])
    except:
        print("could not fetch")
        continue

    yes = False
    for term in banned:
        if term in data["url"] or term in data["catagory"]:
            yes = True
            break
    if yes:
        print("banned")
        continue

    y, x, _ = img.shape
    if x < 600 or y < 600:
        print("too small")
        continue

    print("yes")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)

    found = []

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
                        corners[i][0], corners[j][0], corners[k][0])
                    direction = math.dist(
                        corners[i][0], corners[k][0]) - math.dist(corners[i][0], corners[j][0])

                    if ratio >= 1.60 and ratio <= 1.62 and diff >= 0 and diff <= .4 and direction > 0:
                        found.append([i, j, k])

    for f in found:
        print("found")
        insert = """
        INSERT INTO
            golden (url, catagory, x1, y1, x2, y2, x3, y3)
        VALUES
            ('{}', '{}', {}, {}, {}, {}, {}, {});
        """.format(data["url"], data["catagory"], str(corners[f[0]][0][0]), str(corners[f[0]][0][1]), str(corners[f[1]][0][0]), str(corners[f[1]][0][1]), str(corners[f[2]][0][0]), str(corners[f[2]][0][1]))
        cur = conn.cursor()
        cur.execute(insert)
        conn.commit()
