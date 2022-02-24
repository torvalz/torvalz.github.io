---
title: Share Folders on Windows VM in KVM
date: 25-02-2022
notetype: feed
---
## Reference
- [How to Enable clipboard and folder sharing in Qemu/KVM on Windows Guest](https://dausruddin.com/how-to-enable-clipboard-and-folder-sharing-in-qemu-kvm-on-windows-guest/) at `dausruddin.com`
## Steps
It did not work on `Tiny10`.
1. Install `Cockpit` and `Cockpit Virtual Machines` on the host machine.
```
sudo apt install cockpit cockpit-machines
```
2. Start the service.
```
sudo systemctl enable cockpit.socket
```
3. Shut down the VM.
4. Add a new hardware as a `channel` named `org.spice-space.webdav.0` to VM in `virt-manager`. 
5. In a `web browser`, connect to **[localhost:9090](http://localhost:9090)** and run the VM.
6. In VM, download ```spice-webdavd``` and install it.
- for 32bit Windows
```
curl https://www.spice-space.org/download/windows/spice-webdavd/spice-webdavd-x86-latest.msi --output spice-webdavd-x86-latest.msi
```
- for 64bit Windows
```
curl https://www.spice-space.org/download/windows/spice-webdavd/spice-webdavd-x64-latest.msi --output spice-webdavd-x64-latest.msi
```
## Tags
#KVM #Windows #filesystem #sharing #Torvalz 