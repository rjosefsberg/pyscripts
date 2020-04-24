import os

base = "/Users/ryan/Utility/convert/fgen/"
delnumber = 50
for dirName, subdirList, fileList in os.walk(base):
    for fl in fileList:
        if delnumber > 0:
            os.remove(dirName + '/' + fl)
            delnumber -= 1
