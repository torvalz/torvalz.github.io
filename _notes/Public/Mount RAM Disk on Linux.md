---
title: Mount RAM Disk on Linux
date: 25-02-2022
notetype: feed
---
I made created and mount RAM disk to `~/Temp`.
## Reference
- [Creating a RAMdisk on Ubuntu - IT Blog](https://ixnfo.com/en/creating-a-ramdisk-on-ubuntu.html)
## Steps
1. Make a directory for RAM disk
```
mkdir ~/Temp
```
2. Mount RAM disk to the directory.
```
sudo mount -t tmpfs -o rw,size=4G tmpfs ~/Temp
```
3. In order to automatically mount it, edit the `fstab`.
```
sudo cp -v /etc/fstab /etc/fstab.backup
sudo nano /etc/fstab
```
4. Add the line to the file.
```
tmpfs  ~/Temp  tmpfs  rw,size=4G  0   0
```
## Experiments
### RAM disk as browser cache of Windows VM
I set the RAM disk to be the cache folder of `Microsoft Edge` on `Windows` VM. It feels sluggish.
## Tags
#RAMdisk #tmpfs #linux #fstab #partition #filesystem #Torvalz 