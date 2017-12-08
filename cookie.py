from flask import Flask,request,make_response,render_template

app=Flask(__name__)

@app.route('/setcookie')
def setcookie():
   resp = make_response(render_template('readcookie.html'))
   resp.set_cookie('name','Rohit')
   resp.set_cookie('age','21')
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('name')
   age = request.cookies.get('age')
   return '<h1>Name:'+name+' <br>Age:'+age+'</h1>'
