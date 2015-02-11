#!/bin/sh
aws s3 sync . s3://www.machinedesignmn.com --recursive --delete --exclude '.git/*' --exclude '.vagrant/*' --exclude 'static/.sass-cache/*' --exclude 'sync.sh' --exclude 'Vagrantfile' --exclude '.gitignore' --exclude 'README.md' --exclude 'dev/*' --exclude 'scripts/*'
