import qrcode
from io import StringIO

from io import BytesIO
from flask import send_file


def random_qr(url='www.google.com'):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    return img

def get_qrimg():
    #img_buf = StringIO()
    #print(type(img_buf))
    img = random_qr()
    raw = BytesIO()
    img.save(raw)

    #img.save(img_buf)
    img.seek(0)
    #return 
    #return send_file(img_buf, mimetype='image/png')

get_qrimg()
