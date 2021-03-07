# Analysis

Now comes the interesting part, the data analysis.

```sql
SELECT COUNT(*) FROM golden
```

`1865`

I ended up with 1865 total occurrences of the golden ratio.

---

```sql
SELECT COUNT(DISTINCT catagory) FROM golden
```

`86`

These were gathered from images from 86 different catagories.

---

```sql
SELECT DISTINCT catagory FROM golden
```

```
sunflower bonsai dent flint pasqueflower meadow yellow beach desert sand trailing red siskiyou bitterroot jewels-of-opar flame woolly heartleaf Arnica woodland Maryland golden brittlebush engelmannia blue daisy orange spreading seaside Philadelphia showy fleabane gaillardia goldenbush heliopsis alpine fall hawkbit edelweiss dense blazing tahoka sticky Mexican long-head prairie nodding butterweed arrowleaf Missouri grey Blue narrow Ohio rough-stemmed tall zigzag goldenrod northern stemless white-rayed Indian pinesap fringed false kitten-tails giant great sulfur maiden blue-eyed golden-beard shrubby narrow-leaf balloon rock cascade wildflower Christmas flowering apomict aquatic cryptogam annual biennial strawberry
```

And these are those catagories.

---

```sql
SELECT COUNT(DISTINCT url) FROM golden
```

`532`

More specifically, these occurrences came from 532 individual images.

---

So, a question I'd like to answer is "What is the most golden ratio-ist image catagory?"

```
python most.py
aquatic has 25 occurrences of the golden ratio with 2 images, bringing it to 12.5 occurrences per image
red has 18 occurrences of the golden ratio with 3 images, bringing it to 6.0 occurrences per image
dent has 11 occurrences of the golden ratio with 2 images, bringing it to 5.5 occurrences per image
sticky has 5 occurrences of the golden ratio with 1 images, bringing it to 5.0 occurrences per image
maiden has 30 occurrences of the golden ratio with 6 images, bringing it to 5.0 occurrences per image
pasqueflower has 34 occurrences of the golden ratio with 7 images, bringing it to 4.857142857142857 occurrences per image
siskiyou has 47 occurrences of the golden ratio with 10 images, bringing it to 4.7 occurrences per image
flint has 14 occurrences of the golden ratio with 3 images, bringing it to 4.666666666666667 occurrences per image
bitterroot has 14 occurrences of the golden ratio with 3 images, bringing it to 4.666666666666667 occurrences per image
beach has 23 occurrences of the golden ratio with 5 images, bringing it to 4.6 occurrences per image
engelmannia has 9 occurrences of the golden ratio with 2 images, bringing it to 4.5 occurrences per image
...
```

One of the big problems with my program is that it goes insane when there is text in the image, and flags about 7 golden ratio occurrences on just that portion. A lot of the top finishers in the above list were there because the photographer had left a watermark. Another problem was images that were completely unrelated and just had a lot of points to draw the golden ratio from. For some reason,  the `dent` and `flint` catagories were just corn, and the kettles triggered a lot of detections.

Yet, I did find a true winner. The Englemannia, a type of daisy, had a bunch of (somewhat) valid detections on not just one but two images.

![engelmannia-591](https://user-images.githubusercontent.com/54278938/110250937-17e41e00-7f4c-11eb-9e40-b2240b72c234.png)

![engelmannia-592](https://user-images.githubusercontent.com/54278938/110250969-4661f900-7f4c-11eb-89e0-4c12e9eee0e2.png)

![engelmannia-593](https://user-images.githubusercontent.com/54278938/110250914-f71bc880-7f4b-11eb-860c-bf5ec8a16fdf.png)]

(This one is questionable)

---

My favorite results from this project though were the sunflowers, which actually have golden ratio detections that humans would find too. With the seeds!

![sunflower-1](https://user-images.githubusercontent.com/54278938/110251066-bc666000-7f4c-11eb-8abf-1ebec45cae37.png)

![sunflower-7](https://user-images.githubusercontent.com/54278938/110251089-d142f380-7f4c-11eb-8e66-de32113a5dac.png)
