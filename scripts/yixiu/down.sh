#!/bin/bash
while read URL
do
	url1=${URL%/*}
	echo $url1
	img_dir="/mnt/usb/pic/${URL:37:12}"
	echo $img_dir
	mkdir -p $img_dir
	for i in {1..50}
	do
	url2=$url1'/'$i'.jpg'
	echo $url2
	wget -c $url2 -P $img_dir
	done
done < img_url
