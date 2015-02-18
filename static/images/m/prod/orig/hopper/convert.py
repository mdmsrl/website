#!/usr/bin/env python
import os, glob, subprocess, shlex

RES = {
        'large_2x': '970x',
        'large': '485x',
        'medium_2x': '1120x',
        'medium': '560',
        'small_2x': '800x',
        'small': '400x'
        }

ORIG_DIR = os.path.dirname(__file__)
NAME = os.path.basename(os.path.realpath(ORIG_DIR))
DEST_DIR = os.path.relpath(os.path.join(ORIG_DIR, '..', '..', NAME))

images = glob.glob(os.path.join(ORIG_DIR, '*.jpg'))
images = map(lambda x: os.path.basename(x), images)

def basename_ext(filename):
    pieces = filename.split('.')
    return '.'.join(pieces[:-1]), pieces[-1]

if os.path.exists(DEST_DIR):
    if not os.path.isdir(DEST_DIR):
        raise ValueError('Destination directory already exists and it\'s a file')
else:
    os.mkdir(DEST_DIR)

plist = []

for image in images:
    basename, ext = basename_ext(image)
    image_src = os.path.relpath(os.path.join(ORIG_DIR, image), os.getcwd())
    for rid, rdata in RES.items():
        destination = os.path.join(DEST_DIR, '{}_{}.{}'.format(basename, rid, ext))
        cmd = "convert -quality 90 -resize {} {} {}".format(rdata, image_src, destination)
        print "Running {}".format(cmd)
        cmd = shlex.split(cmd)
        p = subprocess.Popen(cmd)
        plist.append(p)

for p in plist:
    p.wait()

print 'Finished'
