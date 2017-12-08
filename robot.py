from flask import Flask,redirect
import requests


app=Flask(__name__)

@app.route('/robots.txt')
def view_deny_page():
    return redirect("http://httpbin.org/deny")
