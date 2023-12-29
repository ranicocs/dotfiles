from libqtile import layout
from libqtile.config import Match
from .colors import colors

layouts = [
    layout.MonadTall(margin=12, 
                    border_focus = colors["magenta"],
                    border_normal=colors["dark-grey"]),
    layout.Max(
        margin = 8
    ),
    layout.MonadWide(margin=12, 
                    border_focus = colors["magenta"],
                    border_normal=colors["dark-grey"]),
    layout.Matrix(margin=12, 
                    border_focus = colors["magenta"],
                    border_normal=colors["dark-grey"]),
                    
    # layout.Stack(num_stacks=2,
    #             margin=12, 
    #             border_focus = colors["magenta"],
    #             border_normal=colors["dark-grey"]),
    # layout.Bsp(margin=12, 
    #             border_focus = colors["magenta"],
    #             border_normal=colors["dark-grey"]),
    # layout.Tile(margin=12, 
    #             border_focus = colors["magenta"],
    #             border_normal=colors["dark-grey"]),
    # layout.RatioTile(margin=12, 
    #                 border_focus = colors["magenta"],
    #                 border_normal=colors["dark-grey"]),
    # layout.TreeTab(margin=12, 
    #                 border_focus = colors["magenta"],
    #                 border_normal=colors["dark-grey"]),
    # layout.VerticalTile(margin=12,
    #                 border_focus = colors["magenta"],
    #                 border_normal=colors["dark-grey"]),
    # layout.Zoomy(margin=12, 
    #             border_focus = colors["magenta"],
    #             border_normal=colors["dark-grey"]),
]

floating_layout = layout.Floating(
    border_focus = colors["cyan"],
    border_normal=colors["dark-grey"],
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='pavucontrol'),
    Match(wm_class='pavucontrol-qt'),
    Match(wm_class='blueman-manager'),
    Match(title='nm-connection-editor'),
])
