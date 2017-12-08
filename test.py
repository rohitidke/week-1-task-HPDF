from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route('/authors')
def get_users():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    r1 = requests.get('https://jsonplaceholder.typicode.com/posts')
    json_object=r.json()
    json_object1=r1.json()
    return render_template('authors.html',authors=json_object,posts=json_object1)
