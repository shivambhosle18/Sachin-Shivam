# main program to be run
from BMI import create_app, db
import os


config_name=os.getenv('FLASK_CONFIG','development')
app = create_app(config_name)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)