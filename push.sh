#!/bin/bash

cur_sec=`date '+%s'`
sh sidebar.sh

sleep 1s

git add .
git status

sleep 1s

git commit -m "# $cur_sec"

sleep 1s

git push