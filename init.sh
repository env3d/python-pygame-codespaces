#!/bin/bash

echo "Updating package lists..."
sudo apt update -y
sudo apt install -y tigervnc-standalone-server xvfb fluxbox novnc websockify python3-pip
pip install pygame

echo "Setting up virtual display..."
Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1

echo "Starting VNC server..."
vncserver :2 -geometry 1024x768 -depth 16

echo "Starting Fluxbox window manager..."
fluxbox &

echo "Starting noVNC server..."
websockify --web /usr/share/novnc/ 6080 localhost:5902 &

echo "Setup complete!"
echo "Access noVNC in your browser at: http://$(curl -s ifconfig.me):6080/vnc.html"
