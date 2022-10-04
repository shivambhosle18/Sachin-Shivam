# used for business logic, where api will form
from flask import Blueprint, jsonify, request
from BMI import db
from BMI.models import BMI_data
import json

mod = Blueprint("users",__name__, url_prefix="/")

#######---To Fetch all the data---#######

@mod.route('/', methods = ['GET'])
def fetch_users():
    users=BMI_data.query.all() # select * from User 
    response=[x.__repr__() for x in users]
    return jsonify(response)

#######---To Fetch using perticular ID---#######

@mod.route('/<id>',methods=['GET']) # retrive by id/get by id/fetch by id
def show(id):
    users=BMI_data.query.get(int(id)) # select * from User where user_id=101
    response=users.__bmireturn__()
    update_bmi(int(id),response)
    return jsonify(response)

@mod.route('/update_bmi/<id>/', methods = ['PUT'])
def update_bmi(m,n):
    user=BMI_data.query.get(int(m))
    user.bmi_result=n
    db.session.commit()


# ###############---CRUD OPERTATIONS---###############
#      #######  CREATE OPERATION FROM CRUD  ########

@mod.route('/create_bmi', methods=["POST"])
def create_user1():
    user_data = request.get_json()
    user=BMI_data(
        name=user_data['name'],
        email=user_data['email'],
        weight=user_data['weight'],
        height=user_data['height'],
    )
    db.session.add(user)
    db.session.commit()
    cal=BMI_data.query.get["id"]
    re=cal.id
    return f"User added successfully...id is {re}"
    # POST http://127.0.0.1:5000/user_info/create_user


#######  ADDING DATA USING FORM FORMAT  ########

@mod.route('/create_user_form', methods = ['POST'])
def create_user2():
    name=request.form.get('name')
    email=request.form.get('email')
    weight=request.form.get('weight')
    height=request.form.get('height')
    
    user=BMI_data(
        name=name,
        email=email,
        weight=weight,
        height=height
    )
    db.session.add(user)
    db.session.commit()
    return "User added successfully by form"
    # POST http://127.0.0.1:5000/user_info/create_user_form

