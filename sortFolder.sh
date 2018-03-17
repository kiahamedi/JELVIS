#!/bin/bash 
IFS=$'\n'
clear
files=`ls *mkv`
for i in $files; do
    folders=$( echo "$i" | tr '.' ' ' )
    echo "$folders" 
    mkdir -p "$folders"
    mv "$i" "$folders" 
done
