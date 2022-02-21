---
title : MongoDB
notetype : feed
date : 22-02-2022
---

# Installation
I am trying to install ```MongoDB``` on Ubuntu 20.04 LTS. The current stable version is 5.0, and I refer to [this tutorial](https://thishosting.rocks/install-mongodb-ubuntu/).

## Add the public key
```
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```

## Create MongoDB list
```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

## Update
```
sudo apt update
```

## Install
```
sudo apt-get install mongodb-org
```

## Start the service
```
sudo service mongod start
```

## Autostart
```
sudo systemctl enable mongod
```

# Configuration

1. Open the config file.
```
sudo nano /etc/mongod.conf
```

2. Add IPs to the file.
```
# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1,your.mongodb.server.ip
```

# Data Export
```
mongoexport --uri mongodb+srv://<ID>:<PASSWORD>@<cluster0.rr0th.mongodb.net>/<DBNAME> --collection <COLLECTIONNAME> --out <PATHTOFILE>
```

# Import Data
```
mongoimport --db <DBNAME> --collection <COLLECTIONNAME> --file <PATHTOFILE>
```

# Create User
```
db.createUser({ user: 'tester', pwd: 'tester', roles: [{ role: 'userAdminAnyDatabase', db: 'admin' }] })
```




