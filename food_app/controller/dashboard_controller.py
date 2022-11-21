from flask import render_template, session, redirect, request, flash, jsonify
from flask_bcrypt import Bcrypt
from food_app import app
# import os
from food_app.model.login_model import User
from food_app.model.food_model import Food
from food_app.model.goal_model import Goal
bcrypt = Bcrypt(app)




@app.route('/dashboard')
def dashboard():
  if 'user_id' not in session:
    return redirect('/logout')
  
  data = {
    'id' : session['user_id']
  }
  return render_template('user.html', foods = Food.user(data))




@app.route('/save/food', methods = ['POST'])
def save_food():
  if 'user_id' not in session:
    return redirect('/logout')
  
  data = {
    **request.form,
    "user_id" : session['user_id']
  }
  
  Food.save_food(data)
  return redirect('/dashboard')

@app.route('/sort_date/<date>')
def sort_date(date):
  if "user_id" not in session:
    return redirect('/logout')
  
  user_data = {
    'id' : session['user_id']
  }
  Food.user(user_data)
  
  date = {
    'id' : session['user_id'],
    'date' : date
  }
  foods = Food.group(date)
  return render_template('date.html', foods = foods)


@app.route('/single_date/<date>')
def get_single_date(date):
  if 'user_id' not in session:
    return redirect('/logout')
  
  user_data = {
    'id' : session['user_id']
  }
  Food.user(user_data)
  
  data = {
    'id' : session['user_id'],
    'date' : date
  }


  
  goals = Goal.get_goal(data)
  total_calories = Food.calc_cal(data)
  foods = Food.get_date(data)
  totalGoal = goals['calorie'] - total_calories[0]['calories']
  
  if totalGoal < 0:
    totalGoal = f"You're over your calorie Goal by {abs(totalGoal)}"

  
  return render_template('single_date.html', foods = foods, goals = goals, total_calories = total_calories, totalGoal = totalGoal)
  
  
  

  
  

@app.route('/user/delete/<int:id>')
def delete_meal(id):
  data = {
    'id' : id
  }
  Food.destroy(data)
  return redirect('/dashboard')



# creating a goal app,route for the goal page
@app.route('/create/goal')
def goal_creation():
  return render_template('goal.html')


#  GOAL SAVE ROUTE
@app.route('/save/goal', methods = ['POST'])
def save_goal():
  if 'user_id' not in session:
    return redirect('/logout')
  
  data = {
    **request.form,
    "user_id" : session['user_id']
  }
  
  Goal.save_goal(data)
  return redirect('/dashboard')