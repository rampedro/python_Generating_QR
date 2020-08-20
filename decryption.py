from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

#message = b'encrypt me!'
#s = "sample"
_private_key = b''



def set_msg(s):
    ACCESS_KEY = 'XXXXXXXXXXXXX'
    SECRET_KEY = 'XXXXXXXXXXXXX'    

    mytext = b''
    #if s:
    mytext += bytearray(s, 'utf-8')
    message = mytext



#print("The MSG:")
#print(str(message))

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    #pv = private_key
    _private_key = private_key

    pri = private_key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

    #print("Private key:")
    #print(" THE PRI ")
    #print(pri)
    

    ## Creating a private key file
    with open('private_key3.pem', 'wb') as f:
        f.write(pri)
    
    import boto3
    from botocore.exceptions import NoCredentialsError
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    import random
    n = random.random()
    name = "check" + str(n)
    
    print("********pri**********")
    print(pri)
    

    #pri_transfer = base64.b64encode()
    s3.put_object(Bucket = 'withthem' , Key = name , Body = pri)
    #s3.upload_file(pri_transfer, 'withthem', name)    
    

#    print(pri_transfer)
    print("private key is generated and saved")

## Generating the public key to encrypt the msg 


    public_key = private_key.public_key()


    pub = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


#print("Public key:")
#print(str(pub))
    print("the MSG:")
    print(str(message))

    encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#print("Encrypted MSG:")
#print(encrypted)


## This is how we pass the keys. in Base64

    print("Encrypted:")
    print(str(encrypted))
    
    _str = base64.b64encode(encrypted)

    print(encrypted)
    return _str




def return_encrypted():
    return encrypted

def return_private_key():
    #pvm = base64.b64encode(pv)
    return _private_key
