#!/bin/bash

mouse() {
    xinput disable 11 
}

touchpad() {
    xinput enable 11
}

if lsusb | grep -q "Logitech"; then
    echo "Logitech device detected"
    mouse
else
    echo "No Logitech device detected"
    touchpad
fi