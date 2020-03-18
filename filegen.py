import random
import string
import mimemap
import os
import randomdate

def randomstring(stringLength=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


d = mimemap.MimeMap.simplemimes

base = "/Users/ryan/Utility/convert/fgen/"
for x in range(0, 300):
    fname = base + randomstring() + "." + random.choice(list(d.keys()))
    with open(fname, "wb+") as f:
        print fname
        f.write(" " * random.randint(10, 100))
        setime = randomdate.random_date("1/1/2005 12:00 AM", "1/1/2020 12:00 AM", random.random())
    os.utime(fname, (setime, setime))
