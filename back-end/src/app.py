from flask import Flask, request
import qrcode

app = Flask(__name__)

@app.route("/guest-book", methods=["GET", "POST"])
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


@app.route("/qrcode", methods=["POST"])
def qr_code():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://example.com')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    return send_file("qrcode.png", mimetype="image/png")