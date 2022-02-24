---
title : KVM
notetype : feed
date : 22-02-2022
---

[[Install MongoDB 5.0 in Ubuntu]]

## Reference
https://ubuntu.com/blog/kvm-hyphervisor

## Installation
```
sudo apt -y install bridge-utils cpu-checker libvirt-clients libvirt-daemon qemu qemu-kvm virt-manager
```

## Check the Installation
```
kvm-ok
```

## [Cockpit](http://localhost:9090)
It is a tool for management of VM.

## Trial Logs
### Tiny10 x86
- It is x86 version but works.
- I cannot install ```Microsoft Internet Explorer```.
- I cannot install `Microsoft Office`.
- I installed `.NET Framework` but the OS does not recognize it.
- I cannot install `node-gyp` because the OS does not recognize `.NET Framework` installed.

### Tiny10 x64
- works good, but I can't enable `spice-webdavd`, which is required for file sharing between `KVM` host and guest.

### Windows 11
- I cannot install Windows 11 VM.


