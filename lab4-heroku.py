import os
import sqlite3
from flask import Flask,jsonify,request, send_from_directory

#static website methodok
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'static')
@app.route("/<path:path>",methods=["GET"])
def serveStaticDir(path):
    return send_from_directory(static_file_dir,path)



#database methodok
def initDatabase():
    conn = sqlite3.connect("about.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS person(id INTERGER PRIMARY KEY, name VARCHAR(100), age INTERGER)")
    conn.commit()


def fetchDataFromDatabase():
    with sqlite3.connect("about.db") as conn:
        cur = conn.cursor()
        result = cur.execute("SELECT * FROM person ORDER BY id DESC;").fetchone()
        return jsonify(id = result[0], name = result[1], age = result[2])

def pushDataToDatabase(name,age):
    with sqlite3.connect("about.db") as conn:
        cur = conn.cursor()
        sql = f"INSERT INTO person(name,age) VALUES ('{name}', {age});"
        cur.execute(sql)
        conn.commit()


app = Flask(__name__)
name = "Charles Webex"
age= "140"
@app.route("/api/about", methods = ["POST","GET"])
def about():
    global name,age
    if request.method == "GET":
        return fetchDataFromDatabase()
    elif request.method == "POST":
        req = request.json
        name = req["name"]
        age = req["age"]
        pushDataToDatabase(name,age)
        return jsonify(name = name, age = age)

@app.route("/api/helloworld")
def hello():
    return "Hello World!"

@app.route("/")
def redirectToIndex():
    return app.send_static_file("index.html")


initDatabase()
pushDataToDatabase("Charles Webex", 15)
if __name__ == "__main__":
    app.run()


