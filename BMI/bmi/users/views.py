from flask import Blueprint,jsonify,render_template,request
from bmi import db
from bmi.users.models import Candidate
import json



mod=Blueprint('app_bmi',__name__,url_prefix='/home')

@mod.route('/bmi',methods=['GET'])
def fetch_web():
    return render_template("webp.html")

@mod.route('/calculate_bmi',methods=['GET','POST'])
def calculate_bmi():
    if request.method=="GET":
        return render_template("webp.html")
    if request.method=="POST":
        Candidate_name=request.form.get('Candidate_name')
        Weight=request.form.get('Weight')
        Height=request.form.get('Height')
        user=Candidate(
            Candidate_name=Candidate_name,
            Weight=Weight,
            Height=Height
        )
    db.session.add(user)  
    db.session.commit()
    
