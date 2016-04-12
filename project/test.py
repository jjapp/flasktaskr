# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:57:55 2016

@author: appertjt
"""

#project/test.py

import os
import unittest

from views import app, db
from _config import basedir
from models import User

TEST_DB='test.db'

class AllTests(unittest.TestCase):

    ###########################
    ### setup and teardown #### 
    ###########################
    
    #executed prior to the start of each test
    def setUp(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED']=False
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+\
            os.path.join(basedir, TEST_DB)
        self.app=app.test_client()
        db.create_all()
     
     #executed after each test
    def tearDown(self):
         db.session.remove()
         db.drop_all()
    
    #each test should start with 'test;
    def test_user_setup(self):
        new_user=User("michael", "michael@mherman.org", "michaelherman")
        db.session.add(new_user)
        db.session.commit()
        test=db.session.query(User).all()
        for t in test:
            t.name
        assert t.name=="michael"
        
    def test_form_is_present_on_login_page(self):
        response=self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please sign in to access your task list', response.data)
        
    #unregistered users can't login.
    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password), follow_redirects=True)
    
    def test_users_cannot_login_unless_registered(self):
        response=self.login('foo', 'bar')
        self.assertIn(b'Invalid username or password', response.data)
        
    #Registered users can login (form validation)
    def register(self, name, email, password, confirm):
        return self.app.post('register/', data=dict(name=name, email=email, password=password, confirm=confirm),follow_redirects=True)
    
    def test_users_can_login(self):
        self.register('Michael', 'michael@realpython.com', 'python','python')
        response=self.login('Michael', 'python')
        self.assertIn('Welcome', response.data)
    
    def test_invalid_form_data(self):
        self.register('Michael', 'michael@realpython.com', 'python', 'python')
        response=self.login('alert("alert box!");', 'foo')
        self.assertIn(b'Invalid username or password.', response.data)
        
    #form is present on register page    
    def test_form_is_present_on_register_page(self):
        response=self.app.get('register/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please register to access the task list.', response.data)
        
    #users can logout
    def logout(self):
        return self.app.get('logout/', follow_redirects=True)
        
    def test_logged_in_users_can_logout(self):
        self.register('Fletcher', 'fletcher@realpython.com', 'python101', 'python101')
        self.login('Fletcher', 'python101')
        response=self.logout()
        self.assertIn(b'Goodbye!', response.data)
        
    def test_not_logged_in_users_cannot_logout(self):
        response=self.logout()
        self.assertNotIn(b'Goodbye!', response.data)
        
        
    
        
        
            
        
        
if __name__=="__main__":
    unittest.main()
    
         
            
        
        