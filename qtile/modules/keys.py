from libqtile import layout
from libqtile.lazy import lazy
from libqtile.config import Key
from .to_import import *


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.next_screen(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow(),
        desc="Grow window"),
    Key([mod, "control"],
        "l",
        lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split andñ unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "q", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Floating
    Key([mod], "f", lazy.window.toggle_floating()),

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Rofi
    Key([mod], "Tab", lazy.spawn(rofi)),
    Key([alt], "Tab", lazy.spawn(rofi_windows)),
    Key([mod, alt], "Tab", lazy.spawn(rofi_power)),
    Key([mod], "e", lazy.spawn(rofi_emoji)),


    # Brightness
    Key([], brightnessUp, lazy.spawn("brightnessctl set +10%")),
    Key([], brightnessDown, lazy.spawn("brightnessctl set 10%-")),

    # Volume
    Key([], raiseVolume,lazy.spawn("amixer set Master 5%+")),
    Key([], lowerVolume,lazy.spawn("amixer set Master 5%-")),
    Key([], mute,lazy.spawn("amixer set Master toggle")),

    # Media
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),

    # Screenshot
    Key([mod], "Print", lazy.spawn(screenshot_gui)),
    Key([], "Print", lazy.spawn(screenshot)),
]
