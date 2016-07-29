for i in $(seq 0 4999);do 
    out=$(echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i" | nc localhost 30002)
    if [ $(echo $out | grep -c Wrong) -gt 0 ];then
        printf '.'
    else
	echo '#######################'
        echo $out
	echo '#######################'
	exit
    fi
done
