from flask import Blueprint, request, send_file
import qrcode

app_qrcode = Blueprint('qrcode',__name__)

@app_qrcode.route("/qrcode", methods=["POST"])
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