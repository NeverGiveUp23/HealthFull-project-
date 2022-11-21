from food_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# class user like in SQL database
class User:
  def __init__(self,db_data):
    self.id = db_data['id']
    self.first_name = db_data['first_name']
    self.last_name = db_data['last_name']
    self.email = db_data['email']
    self.password = db_data['password']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    
    # CREATING QUERY TO SAVE THE USERS INFO
  @classmethod
  def save(cls, data):
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
    return connectToMySQL('healthfull').query_db(query, data)
  
  #  FETCHING THE EMAIL FROM THE USERS INPUT
  @classmethod
  def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('healthfull').query_db(query,data)
        if len(results) < 1:
            return False
        return User(results[0])
      
      
      #  STATIC METHOD FOR USER VALIDATION
  @staticmethod
  def validate_user(users):
    valid = True
    if len(users['first_name']) < 2:
      valid = False
      flash('First name must be at least 3 characters.', "register")
    if len(users['last_name']) < 2:
      valid = False
      flash('Last name must be at least 3 characters.', "register")
      #  inputting email regex to see if it matches the code for a valid email
    if not EMAIL_REGEX.match(users['email']):
      flash('Invalid Email Address.', "register")
      valid = False
      
    query = "SELECT * FROM users WHERE email = %(email)s;"
    results = connectToMySQL('healthfull').query_db(query, users)
    if len(results) >= 1:
      flash('Unavailable Email Address.', "register")
      valid = False
      
    if len(users['password']) < 8:
      valid = False
      flash('Password must be 8 characters long.', "register")
      # this is checking to see if the password the user input is the same when they confirm it.
    if users['password'] != users['confirm_password']:
      valid = False
      flash('Password does not match!', "register")
      
    return valid