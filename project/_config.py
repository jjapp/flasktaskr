# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 08:02:04 2016

@author: appertjt
"""

import os

#grab the folder where this script lives
basedir=os.path.abspath(os.path.dirname(__file__))

DATABASE='flastaskr.db'
CSRF_ENABLED=True
SECRET_KEY='my_precious'

#define the full path for the database

DATABASE_PATH=os.path.join(basedir, DATABASE)

#the database uri
SQLALCHEMY_DATABASE_URI='sqlite:///'+DATABASE_PATH
