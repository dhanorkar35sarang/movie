# integrate html with flask # also known as jinja2
## HTTP verb GET and POST 





from flask import Flask 
from flask import redirect , url_for , render_template , request


app = Flask(__name__)


@app.route('/') # decorattor
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
   res=""
   if score >=50:
       res="PASS"
   else:
       res="FAIL"
   return render_template('result.html',result=res)

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


# result checker HTML page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score  = 0 
    if request.method=='Post':
        science = float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    
    res=""

    return redirect(url_for('success',score=total_score))




if __name__=='__main__':
    app.run(debug=True)