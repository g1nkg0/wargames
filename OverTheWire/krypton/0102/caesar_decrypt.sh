#!/bin/bash
cat $1 | tr MNOPQRSTUVWXYZABCDEFGHIJKL ABCDEFGHIJKLMNOPQRSTUVWXYZ > $1.decrypt
