HackPrinceton
=============

CMU representing at HackPrinceton 2013!
Who knows what we'll make :D
Here we are!

Team
----
- [Oscar Bezi](http://www.oscarbezi.com)
- Sinan Cepel
- Andre Jia
- [Jake Zimmerman](http://www.jacobzimmerman.me)


TODO: Hopefully updated hourly
==============================

General:
--------
- favicon.ico
- add analytics
- accent colors for palette

Oscar:
------
- Make Django views nice

Jake:
-----
- Get frontend looking nice

Sinan:
------
- Mongo stuff and importing SailThru data

Andre:
------
- Getting up to speed with Django

Instructions for MongoDB
========================
Installation
------------
If you have `brew` installed (like every Mac user should):
- `brew install mongodb`

If you don't, then it's a bit trickier:
- Download from www.mongodb.org/downloads
- Go to folder with download

```bash
    $ tar -zxvf mongodb-osx-x86_64-2.4.8.tgz
    $ sudo mv mongodb-osx-x86_64-2.4.8 /usr/local/mongodb
    $ sudo mkdir -p /data/db
    $ whoami (to find username)
    $ sudo chown username /data/db
```

If you're using Ubuntu:

```bash
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
$ echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
$ sudo apt-get update
$ sudo apt-get install mongodb-10gen
```

- Add the following to .bash\_profile:

```bash
export MONGO_PATH=/usr/local/mongodb
export PATH=$PATH:$MONGO_PATH/bin
```

Regardless of whether or not you have a Mac:
- Install python interface

```bash
pip install pymongo
```

Run and Use
-----------
Follow these instructions to get mongodb up and running
- Mac
    - Terminal 1: `$ mongod`
    - Terminal 2: `$ mongo`
    - Shell will open up (<C-c> to quit)

- Ubuntu

```bash
start:   $ sudo service mongodb start
stop:    $ sudo service mongodb stop
restart: $ sudo service mongodb restart
```
