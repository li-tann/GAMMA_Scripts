#!/bin/bash

CEOS_leader=""
CEOS_data=""
dir=$(ls -l ./ |awk '/^d/ {print $NF}')
for i in $dir
do
    echo $i":"
    files=$(ls -l $i |awk '/^-/ {print $NF}')
    
    for file in $files
    do
        echo -- $file
        # if (grep '^LED' $file)
        # then
        #     CEOS_leader=$file
        # fi
        # if(grep '^IMG-HH' $file)
        # then  
        #     CEOS_data=$file
        # fi
    done

    if (CEOS_leader=="" || CEOS_data=="")
    then
        echo $i a alos2 file
    else     
        echo $i is not alos2 file
    fi
done 

