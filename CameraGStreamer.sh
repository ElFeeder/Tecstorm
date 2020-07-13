#!/bin/bash

raspivid -w 640 -h 360 -n -fps 24 -vf -t 0 -b 200000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=10.132.167.240 port=5000
