#! /usr/bin/bash
if [ "$1" = 1 ]
then
sudo cp -f "/etc/pacman.conf" "/etc/pacman.conf.orig"
sudo sed -i 's/SigLevel.*/SigLevel = Never/' /etc/pacman.conf
fi

if [ "$1" = 0 ]
then
sudo pacman -Syy gnupg archlinux-keyring manjaro-keyring --ignore manjaro-system
sudo mv -f "/etc/pacman.conf.orig" "/etc/pacman.conf"
sudo pacman -Syu
fi
