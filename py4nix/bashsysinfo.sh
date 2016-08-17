#!/usr/bin/env bash

# A script to gather system Information

# Command-1
UNAME="uname -a"
printf "Gathering system information with the $UNAME command: \n\n"
$UNAME

# Command-2
DISKSPACE="df -h"
printf "Gathering system information with the $DISKSPACE command: \n\n"
$DISKSPACE
