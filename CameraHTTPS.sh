#!/bin/bash

raspivid -o - -t 0 -n -w 640 -h 360 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8554}' :demux=h264
