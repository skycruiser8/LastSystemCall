#!/bin/bash
if [[ $1 == "disable" ]]; then
	rmmod snd-hda-intel
	modprobe snd-hda-intel enable=0
elif [[ $1 == "enable" ]]; then
	rmmod snd-hda-intel
	modprobe snd-hda-intel enable=1
else
	echo "1. How to disable audio: sudo ./audio.sh disable"
	echo "2. How to enable audio: sudo ./audio.sh enable"
fi
