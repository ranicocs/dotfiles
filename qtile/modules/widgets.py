from libqtile import widget
from libqtile import qtile
from .colors import colors


widget_defaults = dict(
    font='Fira Code Nerd Font',
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()
class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = f' {self.volume}'
        elif self.volume <= 35:
            self.text = f' {self.volume}'
        elif self.volume < 75:
            self.text = f' {self.volume}'
        else:
            self.text = f' {self.volume}'
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = f'󰆪 {self.volume}'
        elif self.volume <= 35:
            self.text = f' {self.volume}'
        elif self.volume < 75:
            self.text = f' {self.volume}'
        else:
            self.text = f' {self.volume}'
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    fontsize = 13,
    padding_x = 10,
    font='Fira Code Nerd Font',
    background = colors["yellow"],
    foreground = colors["dark-grey"],
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
