
# IMPORTANT KEYS

mod = "mod4"
alt = "mod1"
shift = "shift"
tab = "Tab"
ctrl = "control"
lowerVolume = "XF86AudioLowerVolume"
raiseVolume = "XF86AudioRaiseVolume"
mute = "XF86AudioMute"
brightnessDown = "XF86MonBrightnessDown"
brightnessUp = "XF86MonBrightnessUp"

# ROFI

rofi = "/home/ranicocs/.config/rofi/types/type-7/launcher.sh"
rofi_windows = "/home/ranicocs/.config/rofi/types/type-7/window.sh"
rofi_power = "/home/ranicocs/.config/rofi/powermenu/type-5/powermenu.sh"
rofi_emoji = "/home/ranicocs/.config/rofi/types/type-7/emoji.sh"
rofi_battery = "/home/ranicocs/.config/rofi/applets/bin/battery.sh"

# DEFAULT APPS

editor = "code"
browser = "brave"
terminal = "alacritty"
file_manager = "thunar"
myscelaneous = rofi
notes = "obsidian"
browser2 = "google-chrome-stable"

screenshot = "flameshot screen"
screenshot_gui = "flameshot gui"

# DEFAULT APP FOR EACH WORKSPACE

group_apps = {
    "1": editor,
    "2": browser,
    "3": terminal,
    "4": notes,
    "5": file_manager,
    "6": rofi,
    "7": "steam",
    "8": "spotify",
    "9":browser2
}

def open_default_app(qtile):
    current_group = qtile.current_group.name
    default_app = group_apps[current_group]
    if default_app:
        qtile.cmd_spawn(default_app)