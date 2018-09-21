#!/bin/bash
basedir=`pwd`

##function def
function change_name()
{
cd $1
cnt=1
for file in `ls`
do
	echo $cnt $file
	mv $file $cnt.jpg
	cnt=`expr $cnt + 1 `
done
cd $basedir
}


function identy()
{
cd $1
cnt=1
dis=0
for file in `ls`
do
	info=`identify $file`
#	echo $info
	tmp[0]=`echo $info | cut -d \  -f 1`
	tmp[1]=`echo $info | cut -d \  -f 3`
	echo ${tmp[0]} 	${tmp[1]}
	if [ ${dis[0]} != ${tmp[1]} ] && [ $cnt == 1 ]; then
		dis[0]=${tmp[1]}
		cnt=2
		echo $dis1
	elif [ ${dis[0]} != ${tmp[1]} ] && [ $cnt == 2 ]; then
		dis[1]=${tmp[1]}
		cnt=3
	elif [ ${dis[0]} != ${tmp[1]} ] && [ ${dis[1]} != ${tmp[1]} ] && [ $cnt == 3 ]; then
		dis[2]=${tmp[1]}
		cnt=4
	elif [ ${dis[0]} != ${tmp[1]} ] && [ ${dis[1]} != ${tmp[1]} ] && [ ${dis[2]} != ${tmp[1]} ] && [ $cnt == 4 ]; then
		dis[3]=${tmp[1]}
		cnt=5
#	else 
#	echo "the same display"
	fi
#	cnt=`expr $cnt + 1 `
done
echo ${dis[0]} ${dis[1]} ${dis[2]} ${dis[3]}
}

function deal()
{
	cd $1
	bn=`basename "$PWD"`
	newdir=${bn}_new
	mkdir ../$newdir
	for file in `ls`
	do
		info=`identify $file`
#		echo $info
		tmp[0]=`echo $info | cut -d \  -f 1`
		tmp[1]=`echo $info | cut -d \  -f 3`
#		echo ${tmp[0]} 	${tmp[1]}
	case ${tmp[1]} in 
		"1200x1800")
#			echo "1201x1700"
			convert $file -crop 1200x1700+0+0 ../$newdir/n_$file
			;;
		"1800x1200")
			echo "1800x1101"
			convert $file -crop 1800x1100+0+0 ../$newdir/n_$file
			;;
		"1800x1199")
			echo "1800x1101"
			convert $file -crop 1800x1100+0+0 ../$newdir/n_$file
			;;
		"1199x1800")
			echo "1800x1101"
			convert $file -crop 1199x1700+0+0 ../$newdir/n_$file
			;;

		*)
			echo "no"
			;;
		
	esac
	done
}


change_name $1
identy $1
#deal $1
#convert 30.jpg -crop 1800x1100+0+0 de.jpg
