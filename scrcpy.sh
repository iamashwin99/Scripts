adb kill-server
read -p "Press enter to continue"
adb device
read -p "Press enter to continue"
adb tcpip 5555
read -p "Unplug phone and press enter"

ipadd=$(ip r | grep default| grep wlp| cut -d " " -f 3)

adb connect $ipadd:5555

read -p "Press enter to continue"

scrcpy -s $ipadd:5555 &

