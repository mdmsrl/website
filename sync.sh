#!/bin/sh
aws s3 sync . s3://dev.machinedesignmn.com --recursive --exclude '.git/*' --exclude '.vagrant/*'
