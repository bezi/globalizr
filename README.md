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

Oscar:
------
- Get HTML5Boilerplate with Bootstrap uploaded, work on Javascript for frontend

Jake:
-----
- Get frontend looking nice

Sinan:
------
- Mongo stuff and importing SailThru data

Andre:
------
- Getting up to speed with Django

Instructions for MongoDB:
________________________
Mac: brew update
     brew install mongodb
     If this doesn't work:
     Download from www.mongodb.org/downloads
     go to folder with download
     tar -zxvf mongodb-osx-x86_64-2.4.8.tgz
     sudo mv mongodb-osx-x86_64-2.4.8 /usr/local/mongodb
     sudo mkdir -p /data/db
     whoami
     (username)
     sudo chown username /data/db
     Add /usr/local/mongodb to .bash_profile
     
     export MONGO_PATH=/usr/local/mongodb
     export PATH=$PATH:$MONGO_PATH/bin
     
     pip install pymongo
     
     To run: Terminal 1: mongod
     	     Terminal 2: mongo
	     Shell will open up
     To stop: C-c
Ubuntu: sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
	echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
	sudo apt-get update
	sudo apt-get install mongodb-10gen
To start in Ubuntu: sudo service mongodb start
   stop:    	    sudo service mongodb stop
   restart: 	    sudo service mongodb restart

Windows: Download from www.mongodb.org/downloads
	 Should be obvious :)

To test: python mongotest.py