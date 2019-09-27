sudo ./list.sh
num=$(cat list.txt| cut  -f2|tr -d ')' | tr -d '(' | tr -d "Unknown" |cut -d ' ' -f1|head -$1| tail -1)
sudo ./mac.sh $num

