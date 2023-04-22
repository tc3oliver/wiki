#!/bin/bash
git pull

cur_sec=`date '+%s'`
python sidebar.py

sleep 1s

git add .
git status

sleep 1s

git commit -m "# $cur_sec"

sleep 1s

git push