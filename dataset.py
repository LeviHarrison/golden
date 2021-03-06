import requests

r = requests.get(
    "http://www.image-net.org/api/text/wordnet.structure.hyponym?wnid=n00017222&full=1").text

catagories = r[1:].split('\r\n-')
catagories = catagories[1:len(catagories) - 1]

f = open("dataset.txt", "a")

for catagory in catagories:
    name = requests.get(
        "http://www.image-net.org/api/text/wordnet.synset.getwords?wnid=" + catagory).text.split('\n')[0].split(' ')[0]
    images = requests.get(
        "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + catagory).text.split('\r\n')
    images = images[:len(images) - 1]
    if len(images) < 1:
        continue

    for image in images:
        f.write('{"url": "' + image + '", "catagory": "' + name + '"}\n')

f.close()
