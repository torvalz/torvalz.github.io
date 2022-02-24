---
title: My Pop!_OS 20.04 LTS Setup
date: 24-02-2022
notetype: feed
---
This note is being written for my later use. I am taking notes, developing software, managing Linux servers, and studying linguistics.

## Plan Overview
I plan to build the system for:
- taking notes with **Obsidian**,
- full stack development in **Node.js**,
- Windows desktop app development in **KVM/Qemu**,
- a Hangul(한글) input method,
- connection to my Android phone through **GSConnect**,
- and desktop environment in dark theme.

## Note-taking Environment
I wanted to **take notes anywhere** and **publish** some of them online with `GitHub Pages`.

### Obsidian
- Obsidian is a powerful note-taking app.
- Installed with [AppImage package](https://obsidian.md/download). `Flatpak` version does not support [KIME](https://github.com/Riey/kime).
- [[My Obsidian Setup|Set up Obsidian in my own style]].

### Syncthing
- Syncthing syncs files on various devices. I use it to sync notes taken with Obsidian.
- Installed and set `Syncthing` both on Linux and Android.

## Web Development Environment
Currently, I am developing Vue.js frontend apps and Express.js backend apps.

### Node.js
- [[Install Right Version of Node.js in Linux|Installed the latest LTS version of Node.js]].
- not yet installed `Yarn`.
- not yet installed Vue CLI.

### VS Code
- VS Code is my favorite code editor.
- Downloaded the latest package at [the official website](https://code.visualstudio.com/).

### Lite-XL
- I want to use Lite-XL instead of VS Code.
- Tried several times but not yet satisfactory.

## Windows Desktop Development Environment
I am working on a project which automates Windows.

### KVM/Qemu
- [[Install and Operate KVM|Installed KVM/Qemu]].
- not yet installed Windows VM.

## Hangul Input Method
One of my projects requires Hangul(한글) input.

### KIME
- [[Install KIME in Linux|Installed KIME]].

## Digression
After testing various Linux distros, I decided on `Pop!_OS` as the OS on my dev machine. It is perfect for laptops in that [it manages battery power without any configuration](https://github.com/pop-os/system76-power). It is also based on [Ubuntu](https://ubuntu.com/) , the most widely used Linux distro. In short, it is battery-friendly and stable.

## Tags
#linux #pop-os #Torvalz 
