from flask import Blueprint, request, send_file
import qrcode

guest_book_blueprint = Blueprint('guest_book', __name__)
qrcode_blueprint = Blueprint('qrcode', __name__)


@guest_book_blueprint.route("/guest-book", methods=["GET", "POST"])
def guest_book():
    if request.method == "GET":
        limit = request.args.get("limit")
        if limit:
            # TODO
            return "<p>Hello, World!</p>" + limit
        else:
            return "<p>Hello, World!</p>"

    elif request.method == "POST":
        message = request.json["message"]
        # TODO
        return 'Message saved : "' + message + '"'


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