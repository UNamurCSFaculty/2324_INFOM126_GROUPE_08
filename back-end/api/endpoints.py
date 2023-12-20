from flask import Blueprint, request, send_file
from api.controllers import guest_book_GET, guest_book_POST, qrcode_POST

guest_book_blueprint = Blueprint('guest_book', __name__)
qrcode_blueprint = Blueprint('qrcode', __name__)


@guest_book_blueprint.route("/guest-book", methods=["GET", "POST"])
def guest_book():
    if request.method == "GET":
        # get limit value or get 10 as default value
        limit = request.args.get("limit", 10, type=int)

        return guest_book_GET(limit)

    elif request.method == "POST":
        text = request.json.get("text", None)
        author = request.json.get("author", None)

        if author is None or text is None:
            return {"message": "Invalid request. Both author and text are required."}, 400
        else:
            return guest_book_POST(author, text)


@qrcode_blueprint.route("/qrcode", methods=["POST"])
def qr_code():
    url = request.json["url"]

    img = qrcode_POST(url)
    
    return send_file(img, mimetype="image/png")

