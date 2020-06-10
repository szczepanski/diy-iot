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

   # update and install python3.8 (looong)
   
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
