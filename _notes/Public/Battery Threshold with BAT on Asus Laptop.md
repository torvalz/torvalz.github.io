---
title: Battery Threshold with BAT on Asus Laptop
date: 25-02-2022
notetype: feed
---
## Reference
- https://www.linuxuprising.com/2021/06/easily-set-charging-thresholds-for-asus.html

## BAT command
### 1. Download at the release page
- [Link to GitHub repo page](https://github.com/tshakalekholoane/bat/releases)

### 2. Install
```
sudo install bat /usr/local/bin
```

### 3. Set the threshold to 60
```
sudo bat -t 60
```

### 4.  Make it permanent
```
sudo bat -p
```

## Tags
#battery #Asus #linux #Torvalz


