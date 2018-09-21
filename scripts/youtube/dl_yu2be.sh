#!/bin/bash
echo "=========`date "+%m/%d-%H:%M"`==========" >> data/download_list
flag=0 
while read Line
do
	[[ $Line =~ "no update" ]] || [[ $Line =~ "====" ]] || flag=1
	
	if [[ $flag == 1 ]]; then
		video_id=`echo $Line |cut -d \  -f 3`
		echo $video_id
	fi
	if [[ $flag == 1 ]] && [ `grep -c "$video_id" data/download_list` == '0' ]; then
			echo `date "+%m/%d-%H:%M"`____${video_id:1}  >> data/download_list
			echo "pytube will download"
			python py_scrip/download.py ${video_id:1}
	fi
	flag=0
done < data/id_data
