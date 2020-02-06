#! /bin/bash
INTERFACE="wlan1"
DELAY="2s"

/sbin/ip link set $INTERFACE down
sleep $DELAY;
/sbin/iwconfig $INTERFACE mode monitor
sleep $DELAY;
/sbin/ip link set $INTERFACE up