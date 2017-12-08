Note: Python and Flask should be installed on your system for running this task.</br>
      Download python from https://www.python.org/downloads/ and install.</br>
      For flask, follow this documentation http://flask.pocoo.org/docs/0.12/installation/</br>

Week 1 Task:</br>
1) A simple hello-world at http://localhost:8080/​ that displays a simple string
like "Hello World - Rohit".</br>
Steps for execution:</br>
* Go to folder in which you saved this repo.
* Open cmd by typing cmd in the address bar of this folder.
* In cmd, type : "set FLASK_APP=hello.py" and then hit enter(obviously without double quotation).
* Again type: "flask run" and hit enter.
and it will display as :</br>
 Serving Flask app "hello"</br>
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</br>
* Go to browser and open http://127.0.0.1:5000/ and output will be "Hello World - Rohit".</br>

2)Add a route, for e.g. http://localhost:8080/authors​, which:</br>
a) fetches a list of authors from a request to
https://jsonplaceholder.typicode.com/users</br>
b) fetches a list of posts from a request to
https://jsonplaceholder.typicode.com/posts</br>
c) Respond with only​ a list of authors and the count of their posts (a newline for
each author).</br>
Steps for execution:</br>
* In cmd, type : "set FLASK_APP=test.py" and then hit enter(obviously without double quotation).
* Again type: "flask run" and hit enter.
and it will display as :</br>
 Serving Flask app "test"</br>
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</br>
* Go to browser and open http://127.0.0.1:5000/authors and output will be displayed.</br>
Note: I assumed that you already have opened the cmd and respective directory.</br>

3) Set a simple cookie (if it has not already been set) at
http://localhost:8080/setcookie​ with the following values:
name=<your-first-name> and age=<your-age>.</br>
4) Fetch the set cookie with http://localhost:8080/getcookies​ and display
the stored key-values in it.</br>
Steps for execution:</br>
* In cmd, type : "set FLASK_APP=cookie.py" and then hit enter(obviously without double quotation).
* Again type: "flask run" and hit enter.
and it will display as :</br>
 Serving Flask app "cookie"</br>
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</br>
* Go to browser and open http://127.0.0.1:5000/setcookie and cookie will be set.
* Click the link to go to http://127.0.0.1:5000/getcookie and cookie's key-value will be displayed.</br>

5) Deny requests to your http://localhost:8080/robots.txt​ page. (or you
can use the response at http://httpbin.org/deny if needed)</br>
Steps for execution:</br>
* In cmd, type : "set FLASK_APP=robot.py" and then hit enter(obviously without double quotation).
* Again type: "flask run" and hit enter.
and it will display as :</br>
 Serving Flask app "robot"</br>
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</br>
* Go to browser and open http://127.0.0.1:5000/robots.txt and response at http://httpbin.org/deny will be displayed.</br>
Note: You should internet connection for this task.</br>

6) Render an HTML page at http://localhost:8080/html​ or an image at
http://localhost:8080/image​.</br>
Steps for execution:</br>
* In cmd, type : "set FLASK_APP=render.py" and then hit enter(obviously without double quotation).
* Again type: "flask run" and hit enter.
and it will display as :</br>
 Serving Flask app "render"</br>
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</br>
* Go to browser and open http://127.0.0.1:5000/html and a html page will be rendered.</br>
* Again go to browser and open http://127.0.0.1:5000/image and an image will be rendered.</br>

7) A text box at http://localhost:8080/input​ which sends the data as POST to
any endpoint of your choice. This endpoint should log the received the received to
stdout.</br>
Steps for execution:</br>
* In cmd, type : "set FLASK_APP=input.py" and then hit enter(obviously without double quotation).
* Again type: "flask run" and hit enter.
and it will display as :</br>
 Serving Flask app "input"</br>
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</br>
* Go to browser and open http://127.0.0.1:5000/input.</br>
* There will be one text box. Enter your data in it and hit enter.</br>
* Then your data will be displayed on endpoint http://127.0.0.1:5000/display
