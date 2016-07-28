#!/bin/bash

file=$1

for i in $(seq 1 $(grep -c 'Key: ' $file));do
    line="$(grep 'Key: ' $file)"
    key=${line##Key: }
    key=${key%% Output*}

    if [[ $(echo `python -c "import enchant; d = enchant.Dict('en_US'); print d.check('$key')"`) == True ]];then
        echo '---------------------------'
        echo $line
        echo '---------------------------'
    fi
done
