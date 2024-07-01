
## WSGI APP
## why use WSGI app because to communicate between web server and web application


# Building URLs dynamically
# Variable rule and Url building

from flask import Flask 
from flask import redirect , url_for


app = Flask(__name__)


@app.route('/') # decorattor
def welcome():
    return "welcome to my first project of flask.This is to check wheather it is running or not "

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is " + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is " + str(score)



@app.route('/resultschecker/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='Fail'
    else:
        result='pass'
    return redirect(url_for(result,score=marks))



if __name__=='__main__':
    app.run(debug=True)