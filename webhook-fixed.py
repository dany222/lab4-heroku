import os
import sqlite3
from flask import Flask,jsonify,request, send_from_directory

app = Flask(__name__)

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'static')

@app.route("/<path:path>",methods=["GET"])
def serveStaticDir(path):
    return send_from_directory(static_file_dir,path)
def redirectToIndex():
    return app.send_static_file("index.html")

@app.route("/api/bot", methods = ['POST'])
def hook():
        webhookMessage = request.json
        print (webhookMessage)
        messageId = webhookMessage["data"]["id"]
        print (messageId)
        return jsonify(webhookMessage)

if __name__ == "__main__":
        app.run()


