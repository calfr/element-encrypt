from html import parser
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util import Padding
from bs4 import BeautifulSoup
import importlib.resources
import secrets, base64

def encrypt_html(html: str, key: str, iv: bytes = None, key_salt: bytes = None):
    if key_salt is None:
        key_salt = secrets.token_bytes(16)
    derived_key = PBKDF2(key, count=13337, salt=key_salt, dkLen=32)
    if iv is None:
        iv = secrets.token_bytes(16)
    cipher = AES.new(derived_key, AES.MODE_CBC, IV=iv)
    result = cipher.encrypt(Padding.pad(html.encode("utf-8"),16))
    return base64.b64encode(result), base64.b64encode(iv), base64.b64encode(key_salt)


def populate_template(template_string: str, enc_data: tuple, substitutions = {}):
    result = template_string.replace("%%ENCRYPTED_HTML%%",enc_data[0].decode('utf-8'))\
        .replace("%%IV%%",enc_data[1].decode('utf-8')).replace("%%SALT%%",enc_data[2].decode('utf-8'))
    for (k,v) in substitutions.items():
        result = result.replace(k,v)
    return result


def process_file(file, template=importlib.resources.read_text('elementencrypt','template.html')):
    soup = BeautifulSoup(file,'html.parser')
    # Build a stack to encrypt.

    def stack_build(a, b):
        for result in a.find_all(attrs={"data-elementencrypt-password": True}):
            if result not in b:
                b.insert(0,result)
                stack_build(result,b)
        return b

    stack = stack_build(soup,[])
    for result in stack:
        password = result['data-elementencrypt-password']
        del result['data-elementencrypt-password']
        encrypted_content = encrypt_html(result.prettify(),password)
        result.replace_with(BeautifulSoup(populate_template(template,encrypted_content,{"%%ELEMENT_ID%%":result.get("id",None) or secrets.token_hex(12)}),'html.parser'))
    return soup.prettify()
