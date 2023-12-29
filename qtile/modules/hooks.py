from libqtile import hook, lazy
import subprocess
import os
from libqtile.log_utils import logger

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


@hook.subscribe.client_new
def minecraft_window(window):
    logger.warning(f"New window: {window.name}")
    if "minecraft" in window.name.lower():
        logger.warning(f"Detected Minecraft window: {window.name}")
        window.floating = True  # Activa el modo flotante para ventanas de Minecraft

@hook.subscribe.client_managed
def minecraft_window_managed(window):
    logger.warning(f"Managed window: {window.name}")
    if "minecraft" in window.name.lower():
        logger.warning(f"Managed Minecraft window: {window.name}")
        window.maximized = True  # Maximiza automáticamente las ventanas de Minecraft
        window.fullscreen = True  # Establece la ventana en modo de pantalla completa

@hook.subscribe.client_killed
def minecraft_window_killed(window):
    logger.warning(f"Window killed: {window.name}")
    if "minecraft" in window.name.lower():
        logger.warning(f"Closed Minecraft window: {window.name}")
        window.floating = False  # Desactiva el modo flotante al cerrar ventanas de Minecraft
        window.maximized = False  