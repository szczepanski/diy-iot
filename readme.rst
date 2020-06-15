**DIY IoT**
-------------------

|
|

`back <https://github.com/szczepanski/diy-iot/blob/master/readme.rst>`_

|
|

contents
========

|

.. comment --> depth describes headings level inclusion
.. contents:: .
   :depth: 10

|
|

stepper Motor and HAT setup
===========================

|

.. code:: python

   # update and install python3.8 (duration:1 h)
   
   
   sudo apt-get update
   sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
   wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
   sudo tar zxf Python-3.8.3.tgz
   cd Python-3.8.3
   sudo ./configure --enable-optimizations
   sudo make -j 4
   sudo make altinstall
   echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc
   source ~/.bashrc
   
   #  Configuring I2C
   
   sudo apt-get install -y python-smbus
   
   sudo apt-get install -y i2c-tools
   

components
==========

2 x proximity sensor -> water and feed measuring
1 x camera - Pixy CMUCam-5 

https://pixycam.com/


camera -> tensor flow -> object detection / recognition -> Pixy CMUCam-5 

mic1 -> tensor flow -> sound detection / recognition - inside

mic2 -> tensor flow -> sound detection / recognition - outside


temperature

motion detection  -> number of entries

atmosphere pressure

wind

humidity

light intesity sensors






