import json
import os
#import flask
#from flask 
from flask import Flask, jsonify,request
#from flask 
from flask import send_file

from io import StringIO,BytesIO

from decryption import set_msg,return_private_key

#import sha3
#import base64
import boto3
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)
app.secret_key = 'something_secret'


import qrcode




#s3.Object('withthem', 'ax.jpg').put(Body=open('ax.jpg', 'rb'))

def upload_to_aws(local_file, bucket, s3_file):


    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False



def random_qr(txt):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)

    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image()
    return img

@app.route("/transfer",methods=['GET'])
def transfer():
    user_text = request.args.get('text')
    return jsonify(user_text)


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
    print("KEY!")
    #print(return_private_key) 

    #pri = return_private_key()
    ## Send into AWS
    #with open('myfile2.pem', 'wb') as fd:
    #    fd.write(pri)

    import random
    n = random.random()
    name = str(n) + "file"
    #uploaded = upload_to_aws('private_key2.pem', 'withthem', name)
                                        





    img_buf = BytesIO()
    img.save(img_buf)
    #img_str = base64.b64encode(img_buf.getvalue()).decode()
    img_buf.seek(0)
    #img_str.seek(0)
    return send_file(img_buf, mimetype='image/png')

#@app.route("/pvm",methods=['GET'])
#def pvm():
#    return pv

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


