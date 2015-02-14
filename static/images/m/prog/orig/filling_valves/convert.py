#!/usr/bin/env python
import os, glob, subprocess, shlex

RES = {
        'large_2x': '720x',
        'large': '360x',
        'medium_2x': '500x',
        'medium': '250x',
        'small_2x': '350x',
        'small': '175x'
        }
RES = {
        'large_2x': '800x',
        'large': '400x',
        'medium_2x': '1100x',
        'medium': '550x',
        'small_2x': '750x',
        'small': '375x'
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
        cmd = "convert -quality 65 -resize {} {} {}".format(rdata, image_src, destination)
        print "Running {}".format(cmd)
        cmd = shlex.split(cmd)
        p = subprocess.Popen(cmd)
        plist.append(p)

for p in plist:
    p.wait()

print 'Finished'
