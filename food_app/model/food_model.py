from food_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime
from food_app.model.login_model import User



class Food:
  def __init__(self, db_data):
    self.id = db_data['id']
    self.label = db_data['label']
    self.servings = db_data['servings']
    self.calories = db_data['calories']
    self.protien = db_data['protien']
    self.carbs = db_data['carbs']
    self.date = db_data['date']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    self.user_id = db_data['user_id']
    
    
  @classmethod
  def user(cls, data):
      query = "SELECT * FROM food JOIN users on users.id = user_id WHERE users.id = %(id)s;"
      results = connectToMySQL('healthfull').query_db(query, data)
      foods = []
      for dict in results:
        food = cls(dict)
        user_data = {
          **dict,
          'id' : dict['users.id'],
          'created_at' : dict['created_at'],
          'updated_at' : dict['updated_at']
        }
        users = User(user_data)
        food.user = users
        foods.append(food)
        
      return foods
    
    
    # ================ Saving foods, Goals ======================
  @classmethod
  def save_food(cls, data):
    query = "INSERT INTO food (label, servings, calories, protien, carbs, date, created_at, updated_at, user_id) VALUES (%(label)s, %(servings)s, %(calories)s, %(protien)s, %(carbs)s, %(date)s, NOW(), NOW(), %(user_id)s);"
    return connectToMySQL('healthfull').query_db(query, data)
  
  #  saving the goal
  # @classmethod
  # def save_goal(cls, data):
  #   query = 'INSERT INTO goal (calorie, protien, carb, date, created_at, updated_at, user_id) VALUES (%(calorie)s, %(protien)s, %(carb)s, %(date)s, NOW(), NOW(), %(user_id)s);'
  #   return  connectToMySQL('healthfull').query_db(query, data)
  
  
  # @classmethod
  # def get_goal(cls, data):
  #   query = "SELECT calorie FROM goal JOIN users on users.id = user_id WHERE users.id = %(id)s;"
  #   results = connectToMySQL('healthfull').query_db(query, data)
  #   goals = []
  #   for dict in results:
  #     goal = cls(dict)
  #     goals.append(goal)
  #   return goals
    
  
  
  @classmethod
  def destroy(cls,data):
    query = "DELETE FROM food WHERE id = %(id)s;"
    return connectToMySQL('healthfull').query_db(query,data)
  
  
  @classmethod
  def destroyAll(cls,data):
    query = "DELETE FROM healthfull.food WHERE date = %(date)s AND user_id = %(id)s;"
    return connectToMySQL('healthfull').query_db(query,data)
  
  
  @classmethod
  def group(cls, data):
    query = "SELECT date, sum(calories) as calories, sum(carbs) as carbs, sum(protien) as protien FROM food WHERE user_id = %(id)s GROUP BY date;"
    results = connectToMySQL('healthfull').query_db(query, data)
    return results
  
  @classmethod
  def calc_cal(cls,data):
    query = "SELECT sum(calories) as calories FROM food WHERE user_id = %(id)s AND date = %(date)s;"
    results = connectToMySQL('healthfull').query_db(query,data)
    return results
  
  
  
  @classmethod
  def get_date(cls, data):
    query = "SELECT * FROM food WHERE user_id = %(id)s AND date = %(date)s;"
    result = connectToMySQL('healthfull').query_db(query, data)
    foods = []
    for dict in result:
      food = cls(dict)
      foods.append(food)  
    return foods
  
  # sum every data together to display for the user in a chart
  @classmethod
  def sum_total(cls,data):
    query = " SELECT sum(calories) as calories,sum(servings) as servings, sum(carbs) as carbs, sum(protien) as protien FROM food WHERE user_id = %(id)s;"
    results = connectToMySQL('healthfull').query_db(query, data)
    return results
  
  
#  calories by month
  @classmethod
  def calorie_total_by_month(cls,data):
    query = "SELECT MONTHNAME(date) AS month, SUM(calories) AS calories FROM food JOIN users on users.id = user_id WHERE user_id = %(id)s GROUP BY MONTHNAME(date);"
    results = connectToMySQL('healthfull').query_db(query, data)
    return results
