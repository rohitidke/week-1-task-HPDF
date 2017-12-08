from flask import Flask,request,make_response,render_template

app=Flask(__name__)

@app.route('/input')
def index():
   return render_template('input.html')

@app.route('/display', methods = ['POST', 'GET'])
def display():
   if request.method == 'POST':
       user = request.form['nm']
   return user
