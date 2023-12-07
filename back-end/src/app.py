from flask import Flask, request

app = Flask(__name__)

def guest_book():

    if request.method == "GET":
        limit = request.args.get("limit")
        if limit:
            return "<p>Hello, World!</p>" + limit
        else:
            return "<p>Hello, World!</p>"

    elif request.method == "POST":
        message = request.json["message"]
        return 'Message saved : "' + message + '"'


