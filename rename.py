import glob
import os
for f in glob.glob("yourpathhere*"):
    os.rename(f,f.replace("_"," "))

