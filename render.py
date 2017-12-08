from flask import Flask,render_template

app=Flask(__name__)

@app.route('/html')
def render_html():
    return render_template('sample.html')

@app.route('/image')
def render_image():
    return render_template('img.html')
