from flask import Flask,render_template,request,make_response,redirect
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World - Rohit'

@app.route('/authors')
def get_users():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    r1 = requests.get('https://jsonplaceholder.typicode.com/posts')
    json_object=r.json()
    json_object1=r1.json()
    return render_template('authors.html',authors=json_object,posts=json_object1)

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

@app.route('/robots.txt')
def view_deny_page():
    return redirect("http://httpbin.org/deny")

@app.route('/html')
def render_html():
    return render_template('sample.html')

@app.route('/image')
def render_image():
    return render_template('img.html')

@app.route('/input')
def index():
   return render_template('input.html')

@app.route('/display', methods = ['POST', 'GET'])
def display():
   if request.method == 'POST':
       user = request.form['nm']
   return user
