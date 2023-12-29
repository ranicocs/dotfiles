from libqtile.config import Screen
from .to_import import *
from .bars import *

# #
# #   SCREENS
# #

screens = [
    Screen(top=screen2_bar),
    Screen(top=screen1_bar),
]
