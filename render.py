import sqlite3
import cv2
from skimage import io

conn = sqlite3.connect("./db.sqlite3")
cur = conn.cursor()
cur.execute("SELECT * FROM golden")

images = cur.fetchall()

for image in images:
    try:
        img = io.imread(image[1])
    except:
        continue

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.line(img, (image[3], image[4]), (
        image[5], image[6]), (0, 0, 225), 7)
    img = cv2.line(img, (image[5], image[6]),
                   (image[7], image[8]), (255, 0, 0), 7)

    filename = f"renders/{image[2]}-{image[0]}.png"
    cv2.imwrite(filename, img)
