#!/bin/sh
aws s3 sync . s3://www.mdm-srl.com --size-only --delete --exclude '.git/*' --exclude 'static/.sass-cache/*' --exclude '.gitignore' --exclude 'README.md'
