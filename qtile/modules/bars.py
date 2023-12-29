from libqtile import widget, bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from .to_import import *
from .colors import colors
from .widgets import volume


# #
# #   POWERLINES
# #

rounded_powerlineRight = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_right",
            size=11,
        )
    ]
}
rounded_powerlineLeft = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_left",
            size=11,
        )
    ]
}

# #
# #   BARS
# #

screen1_bar = bar.Bar(
    [
        #
        #   WIDGETS
        #
        widget.Sep(padding=3,
                    linewidth=0,
                    background = colors["transparent"],
                    **rounded_powerlineRight
                    ),
        widget.TextBox(
            text = "󰣇",
            font="FiraCode Nerd Font Mono",
            fontsize=30,
            padding_x=3,
            padding_y=6,
            foreground=colors["white"],
            background=colors["violet"],
            mouse_callbacks= {"Button3": lazy.spawn(rofi_power),
                                "Button1": lazy.spawn(rofi)}
        ),
        widget.Sep(
                    padding=3,
                    linewidth=0,
                    background = colors["violet"],
        ),
        widget.TextBox(
            text = "|",
            foreground=colors["white"],
            background=colors["violet"],
            font="FiraCode Nerd Font Mono",
            fontsize = 20,
        ),
        widget.CurrentLayoutIcon(
            padding=3,
            scale=0.5,
            background = colors["violet"],
            foreground = colors["dark"],
            **rounded_powerlineLeft,
        ),
        widget.Spacer(
            length=10,
            **rounded_powerlineRight
        ),
        widget.GroupBox(
                
            font="FiraCode Nerd Font Mono",
            fontsize = 30,
            padding_x = 3,
            padding_y = 3,
            rounded = False,
            center_aligned = True,
            disable_drag = False,
            borderwidth = 3,
            highlight_method = "line",

            active = colors["violet"],
            inactive = colors["white"],
            highlight_color = colors["dark-grey"],
            this_current_screen_border = colors["violet"],
            this_screen_border = colors["purple"],
            other_screen_border = colors["purple"],
            other_current_screen_border = colors["blue"],
            background = colors["dark-grey"],
            foreground = colors["row"]["5"],
            opacity = 0-95,

            **rounded_powerlineLeft,
        ),
        widget.TaskList(
            margin=0,
            padding=6,
            icon_size=0,
            fontsize=12,
            borderwidth=1,
            title_width_method="uniform",
            urgent_alert_methond="border",
            foreground = colors["white"],
            background = "00000000",
            border = "00000000",
            urgent_border = colors["red-alt"],
            txt_floating = " ",
            txt_maximized = " ",
            txt_minimized = " ",
            mouse_callbacks = {"Button3": lazy.window.kill()}
        ),
        widget.Systray(
            # padding_x = 15,
            icon_size=16,
        ),
        widget.Spacer(
            length=5,
            **rounded_powerlineRight,
        ),
        widget.TextBox(
            text = "󰃰",
            foreground=colors["yellow"],
            background=colors["dark-grey"],
            font="FiraCode Nerd Font Mono",
            fontsize = 18  
        ),
        widget.Clock(
            padding=5,
            format="%a %d %b %H:%M",
            foreground=colors["yellow"],
            background=colors["dark-grey"],
            mouse_callbacks = {"Button3": lazy.spawn('brave https://calendar.google.com/calendar/u/0/r/month?pli=1')},
            **rounded_powerlineLeft,
        ),
        widget.Spacer(
            length = 8,
            **rounded_powerlineRight,
        ),
        # widget.PulseVolume(
        #     fmt="󰕾 {}",
        #     foreground=colors["dark"],
        #     background=colors["yellow"],
        #     padding=10,
        #     font="FiraCode Nerd Font Mono",
        #     mouse_callbacks = {"Button3": lazy.spawn("pavucontrol")},
        # ),
        # widget.PulseVolumeExtra(
        #     fmt="󰕾 {}",
        #     foreground=colors["dark"],
        #     background=colors["yellow"],
        #     padding=10,
        #     font="FiraCode Nerd Font Mono",
        #     mouse_callbacks = {"Button3": lazy.spawn("pavucontrol")},
        # ),
        widget.TextBox(
            text = "|",
            foreground=colors["dark"],
            background=colors["yellow"],
            font="FiraCode Nerd Font Mono",
        ),
        widget.WiFiIcon(
            active_colour = colors["dark-grey"],
            inactive_colour = colors["grey"],
            foreground=colors["dark"],
            background=colors["yellow"],
            padding=10,
            font="FiraCode Nerd Font Mono",
            mouse_callbacks = {"Button3": lazy.spawn("nm-connection-editor")},
        ),
        widget.TextBox(
            text = "|",
            foreground=colors["dark"],
            background=colors["yellow"],
            font="FiraCode Nerd Font Mono",
        ),
        widget.Battery(
            format = '{percent:2.0%}',

            foreground=colors["dark"],
            background=colors["yellow"],
            mouse_callbacks = {"Button3": lazy.spawn(rofi_battery)}
        ),
        widget.UPowerWidget(
            battery_name = "BAT0",
            battery_height = 8,
            battery_width = 15,
            border_charge_colour = colors["dark"],
            border_colour = colors["dark"],
            border_critical_colour = colors["red"],
            fill_charge = colors["dark"],
            fill_critical = colors["red"],
            fill_low = colors["dark"],
            fill_normal = colors["dark"],

            foreground=colors["dark"],
            background=colors["yellow"],
            mouse_callbacks = {"Button3": lazy.spawn(rofi_battery)}
        ),
        widget.Sep(
            foreground=colors["yellow"],
            background=colors["yellow"],
            **rounded_powerlineLeft
        )
    ],
    30,
    margin=[6,   # Positive Y
            10,   # Positive X
            0,   # Negative Y
            10],  # Negative X

    border_width=[0, 0, 0, 0],
    background= colors["transparent"],
)

screen2_bar = bar.Bar(
    [
        #
        #   WIDGETS
        #
        widget.Sep(padding=3,
                    linewidth=0,
                    background = colors["transparent"],
                    **rounded_powerlineRight
        ),
        widget.TextBox(
            text = "󰣇",
            font="FiraCode Nerd Font Mono",
            fontsize=28,
            padding_x=3,
            padding_y=6,
            foreground=colors["white"],
            background=colors["violet"],
            mouse_callbacks= {"Button3": lazy.spawn(rofi_power),
                                "Button1": lazy.spawn(rofi)}
        ),
        widget.Sep(
                    padding=3,
                    linewidth=0,
                    background = colors["violet"],
        ),
        widget.TextBox(
            text = "|",
            foreground=colors["white"],
            background=colors["violet"],
            font="FiraCode Nerd Font Mono",
            fontsize = 20,
        ),
        widget.CurrentLayoutIcon(
            padding=3,
            scale=0.5,
            background = colors["violet"],
            foreground = colors["dark"],
            **rounded_powerlineLeft,
        ),
        widget.Spacer(
            length=10,
            **rounded_powerlineRight
        ),
        widget.GroupBox(
                
            font="FiraCode Nerd Font Mono",
            fontsize = 30,
            padding_x = 3,
            padding_y = 3,
            rounded = False,
            center_aligned = True,
            disable_drag = False,
            borderwidth = 3,
            highlight_method = "line",

            active = colors["violet"],
            inactive = colors["white"],
            highlight_color = colors["dark-grey"],
            this_current_screen_border = colors["violet"],
            this_screen_border = colors["purple"],
            other_screen_border = colors["purple"],
            other_current_screen_border = colors["blue"],
            background = colors["dark-grey"],
            foreground = colors["row"]["5"],
            opacity = 0-95,
            mouse_callbacks = {"Button3": lazy.function(open_default_app)},

            **rounded_powerlineLeft,
        ),
        widget.TaskList(
            margin=0,
            padding=6,
            icon_size=0,
            fontsize=12,
            borderwidth=1,
            title_width_method="uniform",
            urgent_alert_methond="border",
            foreground = colors["white"],
            background = "00000000",
            border = "00000000",
            urgent_border = colors["red-alt"],
            txt_floating = " ",
            txt_maximized = " ",
            txt_minimized = " ",
            mouse_callbacks = {"Button3": lazy.window.kill()}
        ),
        widget.Systray(
            # padding_x = 15,
            icon_size=16,
        ),
        widget.Spacer(
            length=5,
            **rounded_powerlineRight,
        ),
        widget.TextBox(
            text = "󰃰",
            foreground=colors["yellow"],
            background=colors["dark-grey"],
            font="FiraCode Nerd Font Mono",
            fontsize = 18  
        ),
        widget.Clock(
            padding=5,
            format="%a %d %b %H:%M",
            foreground=colors["yellow"],
            background=colors["dark-grey"],
            mouse_callbacks = {"Button3": lazy.spawn('brave https://calendar.google.com/calendar/u/0/r/month?pli=1')},
            **rounded_powerlineLeft,
        ),
        widget.Spacer(
            length = 8,
            **rounded_powerlineRight,
        ),
        volume,
        widget.TextBox(
            text = "|",
            foreground=colors["dark"],
            background=colors["yellow"],
            font="FiraCode Nerd Font Mono",
        ),
        widget.CPU(
            format=" {load_percent}%",
            foreground=colors["dark"],
            background=colors["yellow"],
            mouse_callbacks={"Button3": lazy.spawn("gnome-system-monitor")},
        ),
        widget.TextBox(
            text = "|",
            foreground=colors["dark"],
            background=colors["yellow"],
            font="FiraCode Nerd Font Mono",
        ),
        widget.Memory(
            fmt=" {}",
            format = "{MemUsed:.0f}{mm} {MemPercent:.0f}%",
            measure_mem='M',
            foreground=colors["dark"],
            background=colors["yellow"],
        ),
        # widget.TextBox(
        #     text = "|",
        #     foreground=colors["dark"],
        #     background=colors["yellow"],
        #     font="FiraCode Nerd Font Mono",
        # ),
        # widget.ThermalSensor(
        #     fmt=" {}",
        #     foreground=colors["dark"],
        #     background=colors["yellow"],
        #     threshold=90,  # Puedes ajustar este valor según tu preferencia
        # ),
        widget.Sep(
            foreground=colors["yellow"],
            background=colors["yellow"],
            **rounded_powerlineLeft
        )
    ],
    28,
    margin=[5,   # Positive Y
            9,   # Positive X
            0,   # Negative Y
            9],  # Negative X

    border_width=[0, 0, 0, 0],
    background= colors["transparent"],
)
