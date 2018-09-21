#!/bin/bash
source privoxy_rc

echo "=========`date "+%F-%H:%M"`=========="
echo "=========`date "+%F-%H:%M"`==========" >> data/id_data
while read URL
do
	python py_scrip/v3det.py $URL  #2 parameters in URL
done < data/url_data
./dl_yu2be.sh
