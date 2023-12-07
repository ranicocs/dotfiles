# dotfiles


### Info

- **OS**: [EndeavourOS Qtile](https://discovery.endeavouros.com/window-tiling-managers/qtile/)
- **Window Manager:** [Qtile](#Qtile)
- **Launcher:** [Rofi](#Rofi)
- **Compositor:** [Picom Jonaburg](https://github.com/jonaburg/picom)
- **Terminal:** [Alacritty](#Terminal)
- **Lockscreen:** [betterlockscreen](https://github.com/betterlockscreen/betterlockscreen)
- **File Manager:** thunar
- **GTK Theme**: [yaru-magenta-dark](https://aur.archlinux.org/packages/yaru-gtk-theme)
- **Notifications**: [dunst](https://github.com/dunst-project/dunst)
- **Fonts:**  FiraCodeNerdFont, CaskaydiaCoveNerdFont, CascadiaCode, OpenSans, liberation, noto

## Qtile

* [Qtile](qtile.org)
* [Qtile Extras](https://github.com/elParaguayo/qtile-extras)
* `~/.config/qtile`
### Keybindings




### Default Apps

* **Editor** -> VSCode
- **Browser** -> Brave
- **Terminal Emulator** -> Alacritty
- **File Manager** -> Thunar
- **Notes** -> Obsidian
- **Browser2** -> Google Chrome

-  **Workspace default app**: 
	- "1": editor
	- "2": browser,
	- "3": terminal,
	- "4": notes,
	- "5": file_manager,
	- "6": rofi,
	- "7": "steam",
	- "8": "spotify",
	- "9":browser2

## Fonts

```
yay -S ttf-bitstream-vera ttf-cascadia-code ttf-cascadia-code-nerd ttf-dejavu ttf-firacode-nerd ttf-liberation ttf-nerd-fonts-symbols ttf-nerd-fonts-symbols-common ttf-opensans noto-fonts noto-fonts-emoji
```

## Cursor

```
yay -S bibata-cursor-theme-bin
cd /usr/share/icons/default
sudo nano index.theme
# [Icon Theme]
# Inherits=Bibata-Modern-Classic
```



## Rofi
[Rofi]()

## Terminal
### Terminal Emulator
* [**Alacritty**](https://github.com/alacritty/alacritty)
* `~/.config/alacritty/alacritty.yml`

### Shell
* [**Zsh**](https://zsh.org) 
* `~/.config/zsh/.zshrc`
- **Plugins**
	- [Autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
	- [Shift Select](https://github.com/jirutka/zsh-shift-select)
	- [Syntax Highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

### Prompt
* [**Starship**](https://starship.rs/)
* `~/config/starship.toml`
### Neofetch
* [**Neofetch**](https://github.com/dylanaraps/neofetch)
* `/.config/neofetch/config.conf`
- **Theme** -> [Neofetch themes](https://github.com/Chick2D/neofetch-themes)
### Some useful packages

| Package Name                                                                        | Description                | Package Manager |
| ----------------------------------------------------------------------------------- | -------------------------- | --------------- |
| [ bat ](https://github.com/sharkdp/bat)                 | cat clone       | pacman          |
| [ lsd ](https://github.com/lsd-rs/lsd)     | ls clone               | pacman          |
| [ btm ](https://github.com/ClementTsang/bottom)     | system monitor               | pacman          |
| [ yay ](https://github.com/Jguer/yay)     | AUR helper               | pacman          |

## Other themes
- **Lightdm** -> [glorious](https://github.com/eromatiya/lightdm-webkit2-theme-glorious)
- **GTK Theme** -> [yaru-magenta-dark](https://aur.archlinux.org/packages/yaru-colors-gtk-theme)

## Screenshots

![Qtile](./screenshot1.png)
![Qtile](./screenshot2.png)
![Qtile](./screenshot3.png)

