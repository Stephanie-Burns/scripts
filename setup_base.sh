#!/bin/bash

# Update the system
sudo pacman -Syu --noconfirm

# Install essential packages
sudo pacman -S --noconfirm base-devel vim git curl wget zsh htop neofetch sudo

# Configure sudo
echo "%wheel ALL=(ALL) ALL" | sudo tee -a /etc/sudoers
sudo usermod -aG wheel $USER

# Change default shell to zsh
sudo pacman -S --noconfirm zsh
chsh -s $(which zsh)

# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install yay (AUR helper)
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si --noconfirm
cd ..
rm -rf yay

# Install development tools
sudo pacman -S --noconfirm python python-pip nodejs npm docker code

# Install pipx using pacman
sudo pacman -S --noconfirm python-pipx

# Install argcomplete using pip
python -m pip install --user argcomplete

# Ensure pipx is available in the PATH
python -m pipx ensurepath

# Setup argcomplete for pipx in zsh
autoload -U compinit && compinit
eval "$(register-python-argcomplete pipx)"

# Configure .zshrc
cat << 'EOF' > ~/.zshrc
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
plugins=(git)
source $ZSH/oh-my-zsh.sh
alias ll='ls -la'
EOF

# Set up SSH keys
ssh-keygen -t rsa -b 4096 -C "stephanieburns302@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
echo "Add this SSH key to your GitHub account:"
cat ~/.ssh/id_rsa.pub

echo "Setup complete! Please restart your terminal."

