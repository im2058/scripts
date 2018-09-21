#!/bin/bash
# for auto mount usb>>/mnt/usb for samba
usb=`ls /dev/sd*4`
sudo mount -t vfat -o umask=000 $usb /mnt/usb

# for youtube download
source /home/pi/KK/youtube/privoxy_rc
sslocal -c /etc/shadowsocks/config.json &  >> sslocal.log
