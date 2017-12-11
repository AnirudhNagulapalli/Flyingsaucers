'''
This file is used to define the functionalities of User API
@author: Anirudh Nagulapalli, Kavya Reddy Vemula
'''

import connexion
import MySQLdb
from swagger_server.models.user import *
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

#Connecting to the database
mysql_cn= MySQLdb.connect(host='127.0.0.1', 
                port=3306, user='root', passwd='letmein', 
                db='flyingsaucers')

cur = mysql_cn.cursor()



def create_user(body):
    """
    Create user
    This function is used to create a new user. 
    Details are stored in the database
    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())
    #Inserting User data into the User table of the Flyingsaucer database
    cur.execute("INSERT INTO users VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(body.email, body.first_name, body.last_name, body.password, body.phone, body.user_status, body.username, body.id))
    mysql_cn.commit()
    return 'User created with the username ' +body.username



def delete_user(username):
    """
    Delete user
    This function is used to delete the user
    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    cur.execute("DELETE FROM users WHERE username=%s",[username])
    mysql_cn.commit()
    return 'User ' +username + ' has been deleted'


def get_user_by_name(username):
    """
    This function is used to get the user details based on the given username 
    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
    cur.execute("SELECT * FROM users WHERE username=%s",[username])
    # return 'User found!'
    return cur.fetchall()
    

def login_user(username, password):
    """
    This function lets the user to login to the system
    
    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    #Extracting Username and Password from the database based on the user input values
    cur.execute("SELECT username FROM users WHERE username=%s",[username])
    resultUser = cur.fetchone()[0]
    cur.execute("SELECT password FROM users WHERE username=%s",[username])
    resultPass = cur.fetchone()[0]

    #Checks the user input with the username stored in the database
    if resultUser==username:
        if resultPass==password:
            #Sets the user status to 1 (logged-in state)
            cur.execute("UPDATE users SET userStatus=1 WHERE username=%s",[username])
            mysql_cn.commit()
            return username +' is now logged in'
    else:
        return 'Incorrect/Invalid details'


def logout_user():
    """
    This function lets the user to logout from the system
    

    :rtype: None
    """
    cur.execute("UPDATE users SET userStatus=0")
    return 'You have successfully logged out'


def update_user(username, body):
    """
    This fuction is used to update the user information
    This can only be done by the logged in user.
    :param username: name that need to be updated
    :type username: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())
    cur.execute("SELECT userStatus FROM users WHERE username=%s",[username])
    status = cur.fetchone()[0]
    if status == 1:
        cur.execute("UPDATE users SET email=%s,firstName=%s,lastName=%s,password=%s,phone=%s,userStatus=%s,username=%s,id=%s WHERE username=%s", (body.email, body.first_name, body.last_name, body.password, body.phone, body.user_status, body.username, body.id, [username]))
    mysql_cn.commit()

    return 'Information has been Updated'
