# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd beep extendedglob nomatch
unsetopt notify
# bindkey -v
set noci
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/ranicocs/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

export PATH="$HOME/.cargo/bin/:$HOME/.config/scripts:$PATH"
export JAVA_HOME=/opt/jdk-20.0.2
export PATH=$JAVA_HOME/bin:$PATH
export BROWSER=brave

bindkey "^[[3~" delete-char
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey "\033[1~" beginning-of-line
bindkey "\033[4~" end-of-line

eval "$(starship init zsh)"
eval $(thefuck --alias)

alias ls='lsd --color=auto'
alias grep='grep --color=auto'
alias cat='bat --style=plain --paging=never'
alias cls='clear'
alias pSyu='sudo pacman -Syu'
alias pS='sudo pacman -S'
alias pR='sudo pacman -R'
alias ySyu='yay -Syu'
alias yS='yay -S'
alias yR='yay -R'

alias dotfiles='/usr/bin/git --git-dir=$HOME/git-bare/dotfiles/ --work-tree=$HOME/.config'
alias FIC='/usr/bin/git --git-dir=$HOME/git-bare/FIC --work-tree=$HOME/Dropbox/Obsidian/FIC'
# alias dotfiles-add='dotfiles add alacritty dun'
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.config/zsh/zsh-shift-select/zsh-shift-select.plugin.zsh
