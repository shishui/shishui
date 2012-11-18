import sys
import os
import glob

basedir = sys.argv[1]
files = glob.glob(os.path.join(basedir, '*'))

for fi in files:
    f =  open(fi, 'r')
    content = f.read()
    content = content.rpartition('