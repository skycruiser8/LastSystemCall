#!/bin/bash
if [[ $# -eq 2 ]]; then
    if [[ $1 == "setvolume" ]]; then
        amixer set Master $2%
    else
        echo "How to set volume audio: ./volume.sh setvolume (value)"
    fi
elif [[ $1 == "mute" ]]; then
    amixer set Master mute
elif [[ $1 == "unmute" ]]; then
    amixer set Master unmute
else
    echo "How to set audio volume: ./volume.sh setvolume (value)"
    echo "How to mute audio: ./volume.sh mute"
    echo "How to unmute audio: ./volume.sh unmute"
fi
