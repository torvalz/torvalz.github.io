#!/bin/sh

# Author : Zara Ali
# Copyright (c) Tutorialspoint.com
# Script follows here:

#echo "What is your name?"
#read PERSON
#echo "Hello, $PERSON"

git add .
git commit -m "`date`"
git push origin main
