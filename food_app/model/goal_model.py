from food_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime
from food_app.model.login_model import User
from food_app.model.food_model import Food


class Goal:
  def __init__(self, db_data):
      self.id = db_data['id']
      self.calorie = db_data['calorie']
      self.protien = db_data['protien']
      self.carb = db_data['carb']
      self.date = db_data['date']
      self.created_at = db_data['created_at']
      self.updated_at = db_data['updated_at']
      self.user_id = db_data['user_id']

  @classmethod
  def save_goal(cls, data):
      query = 'INSERT INTO goal (calorie, protien, carb, date, created_at, updated_at, user_id) VALUES (%(calorie)s, %(protien)s, %(carb)s, %(date)s, NOW(), NOW(), %(user_id)s);'
      return connectToMySQL('healthfull').query_db(query, data)



  @classmethod
  def get_goal(cls, data):
      query = "SELECT calorie FROM goal JOIN users on users.id = user_id WHERE users.id = %(id)s AND date = %(date)s;"
      results = connectToMySQL('healthfull').query_db(query, data) 
      try:
        return results[0]
      except IndexError: 
        return None
