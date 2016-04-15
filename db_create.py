# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 08:05:40 2016

@author: appertjt
"""

#db_create.py

from project import db
from project.models import Task, User
from datetime import date


#create the database and the db table
db.create_all()

#insert data
db.session.add(User("admin", "ad@min.com", "admin", "admin"))
db.session.add(Task("finish this tutorial", date(2016, 5, 16), 10, date(2016,2,13),1,1))
db.session.add(Task("Finish Real Python", date(2016, 8, 10), 10, date(2017,3,15),1,1))

# commit the changes
db.session.commit

