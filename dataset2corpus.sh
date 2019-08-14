date
i=0
files=$(find . -name *txt)
n=$(echo $files | wc -w)
for f in $files
do
	cat $f | sed 's/– //g' >> corpus.txt
	echo >> corpus.txt
	echo -ne $i / $n $f "\r"
	i=$((i+1))
	sleep 0.1
done
