import os
import sys
import hashlib

rootDir = '/Users/ryan/Downloads/simflofy-admin/WEB-INF/lib'


def hashfile(paths, blocksize=65536):
    afile = open(paths, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


dups = {}
for dirName, subdirs, fileList in os.walk(rootDir):
    print('Scanning %s...' % dirName)
    for filename in fileList:
        # Get the path to the file
        path = os.path.join(dirName, filename)
        # Calculate hash
        file_hash = hashfile(path)
        # Add or append the file path
        if file_hash in dups:
            dups[file_hash].append(path)
        else:
            dups[file_hash] = [path]

for k,v in dups.iteritems():
    if len(v) > 1:
        print k
        print v
        print ''
