# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 08:05:40 2016

@author: appertjt
"""

#project/db_create.py

from views import db
from models import Task
from datetime import date

#create the database and the db table
db.create_all()

#insert data
db.session.add(Task("finish this tutorial", date(2016, 5, 16), 10, 1))
db.session.add(Task("Finish Real Python", date(2016, 8, 10), 10, 1))

# commit the changes
db.session.commit

