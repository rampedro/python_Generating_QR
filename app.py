import json
import os
from flask import Flask, jsonify,request
from flask import send_file

from io import StringIO,BytesIO

from flask import Flask, jsonify, request
from decryption import set_msg
#import sha3
#import base64


app = Flask(__name__)
app.secret_key = 'something_secret'


import qrcode


def random_qr(txt):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)

    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image()
    return img



@app.route("/",methods=['GET'])
def return_result():
    return jsonify("hi")

@app.route('/get_qrimg',methods=['GET'])
def get_qrimg():
    mytext = b''
    user_text = request.args.get('text') 
    ## Encryptor
    mytext += set_msg(user_text)
    
    #mytext = user_text


    ## hashing user data
    #hash_function = sha3.keccak_256()
    #hash_function.update(mytext)
    #encrypted_text = hash_function.hexdigest()
    img = random_qr(txt=mytext)

    img_buf = BytesIO()
    img.save(img_buf)
    #img_str = base64.b64encode(img_buf.getvalue()).decode()
    img_buf.seek(0)
    #img_str.seek(0)
    return send_file(img_buf, mimetype='image/png')


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


