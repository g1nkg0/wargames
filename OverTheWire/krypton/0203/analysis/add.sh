#!/bin/bash

file11="file1.1"
file21="file2.1"
file31="file3.1"

file12="file1.2"
file22="file2.2"
file32="file3.2"

(
for i in $(seq 0 25);do
    char=`python -c "print chr(ord('A')+$i)"`

    count1=$(grep $char $file11)
    count2=$(grep $char $file21)
    count3=$(grep $char $file31)

    count1=${count1##$char }
    count2=${count2##$char }
    count3=${count3##$char }

    sum=`python -c "print($count1 + $count2 + $count3)"`

    if [[ ${#sum} -lt 3 ]];then
        sum="0$sum"
        if [[ ${#sum} -lt 3 ]];then
            sum="0$sum"
        fi
    fi

    echo "$sum $char"
done
) > sum.analysis.1

(
for i in $(seq 0 25);do
    for j in $(seq 0 25);do
        char1=`python -c "print chr(ord('A')+$i)"`
        char2=`python -c "print chr(ord('A')+$j)"`

        count1=$(grep $char1$char2 $file12)
        count2=$(grep $char1$char2 $file22)
        count3=$(grep $char1$char2 $file32)

        count1=${count1##$char1$char2 }
        count2=${count2##$char1$char2 }
        count3=${count3##$char1$char2 }

        sum=`python -c "print($count1 + $count2 + $count3)"`

        if [[ ${#sum} -lt 3 ]];then
            sum="0$sum"
            if [[ ${#sum} -lt 3 ]];then
                sum="0$sum"
            fi
        fi

        echo "$sum $char1$char2"
    done
done
) > sum.analysis.2
