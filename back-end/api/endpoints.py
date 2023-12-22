import re
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

        if author is None or text is None or not author.strip() or not text.strip():
            message = "Invalid request. Both author and text are required."
            return {"message": message}, 400
        if len(author.strip()) < 3 or len(text.strip()) < 3:
            message = "Invalid request. Both author and text should be at least 2 characters long."
            return {"message": message}, 400
        else:
            return guest_book_POST(author, text)


@qrcode_blueprint.route("/qrcode", methods=["POST"])
def qr_code():
    try:
        url = request.json["url"]
    except KeyError:
        return {"message": "Invalid request. 'url' is required."}, 400
    
    url_regex = re.compile(
        r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$',
        re.IGNORECASE
    )

    if not url_regex.match(url):
        return {"message": "Invalid URL format."}, 400

    img = qrcode_POST(url)

    return send_file(img, mimetype="image/png")
