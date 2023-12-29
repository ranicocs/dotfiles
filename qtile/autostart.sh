#!/bin/sh

# Screens
# screens &
xrandr --output DP-4 --mode 1920x1080 --rate 120.00

# Wallpaper
feh --bg-scale ~/.config/Wallpapers/RoW01.jpg & disown

# Composer
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Lock Screen Randomizer
# betterlockscreen -u $HOME/Wallpapers --fx blur & disown

# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

# Gnome keyring
dbus-update-activation-environment --all &
gnome-keyring-daemon --start --components=secrets &

