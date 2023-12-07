from flask import Blueprint, request

app_guest_book = Blueprint('app_guest_book',__name__)
@app_guest_book.route("/guest-book", methods=["GET", "POST"])
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
