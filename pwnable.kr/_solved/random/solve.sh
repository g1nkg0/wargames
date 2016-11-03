#!/bin/bash
echo $((0xdeadbeef ^ 0x6b8b4567)) | ./random 
