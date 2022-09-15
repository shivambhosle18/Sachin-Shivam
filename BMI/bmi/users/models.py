from flask import jsonify
from bmi import db



class Candidate(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Candidate_name= db.Column(db.String(45),nullable=False)
    Weight= db.Column(db.Float,nullable=False)
    Height= db.Column(db.Float,nullable=False)
    BMI= db.Column(db.Float,nullable=False)

    def __repr__(self):
        return {"id":self.id,"Candidate_name":self.Candidate_name,"Weight":self.Weight,"Height":self.Height,"BMI":self.BMI}