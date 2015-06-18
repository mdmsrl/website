#!/bin/sh
aws s3 sync . s3://dev.machinedesignmn.com --recursive --delete --exclude '.git/*' --exclude 'static/.sass-cache/*' --exclude '.gitignore' --exclude 'README.md' --exclude 'scripts/*'
