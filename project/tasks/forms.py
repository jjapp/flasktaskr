# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:43:26 2016

@author: appertjt
"""

#project/tasks/forms.py

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

class AddTaskForm(Form):
    task_id=IntegerField()
    name=StringField('Task Name', validators=[DataRequired()])
    due_date=DateField('Date Due (mm/dd/yyyy)', validators=[DataRequired()], format='%m/%d/%Y')
    priority=SelectField('Priority', validators=[DataRequired()], choices=[('1','1'),('2','2'), ('3','3'),('4','4'), ('5','5'),('6','6'),
                                                 ('7','7'),('8','8'),('9','9'), ('10','10')])
    status=IntegerField('Status')
    