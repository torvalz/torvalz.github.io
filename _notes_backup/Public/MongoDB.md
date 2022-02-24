---
title : How to Install MongoDB 5.0 in Ubuntu
notetype : feed
date : 22-02-2022
---
# Problem
My `MongoDB Atlas` free tier does not allow for upload anymore because my data size reaches the limit. I have to transfer the DB to a Ubuntu based server.

# Installation
I am trying to install `MongoDB` on `Ubuntu 20.04 LTS`. The latest stable version is 5.0, but `apt install` would not install the latest. So, I refer to [this tutorial](https://thishosting.rocks/install-mongodb-ubuntu/).

## Add the public key
```
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
```

## Create MongoDB list
```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
```

## Update package information
```
sudo apt update
```

## Install MongoDB
```
sudo apt-get install mongodb-org
```

## Start MongoDB service
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
The code below did not work for me.
```
# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1,your.mongodb.server.ip
```

# Data export from MongoDB Atlas
I backed up the data saved on the `MongoDB Atlas` server to new Linux server. The command below will back up a collection into a file.
```
mongoexport --uri mongodb+srv://<ID>:<PASSWORD>@<cluster0.rr0th.mongodb.net>/<DBNAME> --collection <COLLECTIONNAME> --out <PATHTOFILE>
```

# Import data
```
mongoimport --db <DBNAME> --collection <COLLECTIONNAME> --file <PATHTOFILE>
```

# Create user
```
db.createUser({ user: 'tester', pwd: 'tester', roles: [{ role: 'userAdminAnyDatabase', db: 'admin' }] })
```
