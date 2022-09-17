from flask import Flask, render_template

kas = Flask(__name__)

@kas.route('/')
def homepage():
    return render_template('home.html')

if __name__=='__main__':
    kas.run(debug=True)