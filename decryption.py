from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64
#message = b'encrypt me!'
#s = "sample"
def set_msg(s):
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

    pri = private_key.private_bytes(encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

    #print("Private key:")
    #print(str(pri))
    

    ## Creating a private key file
    with open('private_key.pem', 'wb') as f:
        f.write(pri)

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
    print("Encrypted:")
    print(str(encrypted))
    
    _str = base64.b64encode(encrypted)

    print(_str)
    return _str




def return_encrypted():
    return encrypted

def return_private_key():
    return pri
