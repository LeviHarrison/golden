import sqlite3
from operator import itemgetter

conn = sqlite3.connect("./db.sqlite3")
cur = conn.cursor()
cur.execute("SELECT DISTINCT catagory FROM golden")

catagories = cur.fetchall()

results = []
for catagory in catagories:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM golden WHERE catagory='" +
                catagory[0] + "'")
    total = cur.fetchall()[0][0]

    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(DISTINCT url) FROM golden WHERE catagory='" + catagory[0] + "'")
    unique = cur.fetchall()[0][0]

    results.append([catagory[0], total, unique, total / unique])

results.sort(key=lambda x: x[3], reverse=True)
for result in results:
    print(f"{result[0]} has {result[1]} occurrences of the golden ratio with {result[2]} images, bringing it to {result[3]} occurrences per image")
