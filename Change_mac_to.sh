device=$(ip link show | grep wlp | cut -d" " -f2 | tr -d :)
ip link set dev $device down
ip link set dev $device address $1
ip link set dev $device up
