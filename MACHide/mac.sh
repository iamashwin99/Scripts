#sudo arp-scan -l
device=$(ip link show | grep wlp | cut -d" " -f2 | tr -d :)

ip link show |tail |cat > 1.txt


nmcli con down WIFI

ip link set dev $device down
echo "Device is  down :" $device

ip link set dev $device address $1
echo "Device is  set :"

 ip link show |tail |cat > 2.txt

diff 1.txt 2.txt 

ip link set dev $device up
echo "Device is  up :" $device

nmcli con up WIFI
