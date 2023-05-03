#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    >&2 echo "No arguments provided!"
    exit 1
fi

if [ ! -d templates/$1 ]
then
    echo "Directory templates/$1 does not exist!"
    exit 1
fi

echo "Resetting to template: $1 ..."
rm -rf abe/*
cp -R templates/$1/* abe/
git add -A abe/*
git commit -m "Restore template: $1"
echo "... done."

