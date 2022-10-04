# to be used for database connectivity, tables related

from BMI import db

class BMI_data(db.Model): #name of the class and table name should be exactly the same
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40), index=True, unique=True)
    email=db.Column(db.String(120),unique=True)
    weight=db.Column(db.Float)
    height=db.Column(db.Float)
    bmi_result=db.Column(db.Float)

    def __repr__(self):
        return {
            'name':self.name,'email':self.email,'height':self.height,'weight':self.weight,'bmi_result':bmi_result
        }
    
    # def __

    def __bmireturn__(self):
        bmi_result=(self.weight/((self.height)*(self.height)))
        return bmi_result
