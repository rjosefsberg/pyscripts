import random
import string
import mimemap
import os
import randomdate
import shutil


def randomstring(stringLength=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

bits = [" ","i","s","e"]
d = mimemap.MimeMap.simplemimes
makedups = True
dupsize = 33
base = "/Users/ryan/Utility/convert/fgen/"
for x in range(0, 300):
    ext = "." + random.choice(list(d.keys()))
    fname = base + randomstring() + ext
    fsize = random.randint(10, 100)
    setime = randomdate.random_date("1/1/2005 12:00 AM", "1/1/2020 12:00 AM", random.random())
    with open(fname, "wb+") as f:
        f.write(random.choice(bits) * fsize)
    os.utime(fname, (setime, setime))
    if fsize == dupsize and makedups:
        shutil.copyfile(fname, base + 'dups/' + randomstring() + ext)
