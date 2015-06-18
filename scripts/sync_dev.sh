#!/bin/sh
aws s3 sync . s3://dev.machinedesignmn.com --size-only --delete --exclude '.git/*' --exclude 'static/.sass-cache/*' --exclude '.gitignore' --exclude 'README.md' --exclude 'scripts/*'
