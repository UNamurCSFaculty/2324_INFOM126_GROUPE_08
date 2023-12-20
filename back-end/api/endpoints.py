from flask import Blueprint, request, send_file
import qrcode
from controllers import guest_book_GET, guest_book_POST

guest_book_blueprint = Blueprint('guest_book', __name__)
qrcode_blueprint = Blueprint('qrcode', __name__)


@guest_book_blueprint.route("/guest-book", methods=["GET", "POST"])
def guest_book():
    if request.method == "GET":
        # get limit value or get 10 as default value
        limit = request.args.get("limit", 10, type=int)

        return guest_book_GET(limit)

    elif request.method == "POST":
        text = request.json["text"]
        author = request.json["author"]

        return guest_book_POST(author, text)


@qrcode_blueprint.route("/qrcode", methods=["POST"])
def qr_code():
    url = request.json["url"]

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    return send_file("qrcode.png", mimetype="image/png")