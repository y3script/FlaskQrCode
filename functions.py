import qrcode
import io
from base64 import b64encode,b64decode


def decodeData(data):
    DecodedData = b64decode(data)
    return DecodedData


def convert_to_qr(text):
    IoImage = io.BytesIO()
    img = qrcode.make(decodeData(text))
    img.save(IoImage,"PNG")
    return b64encode(IoImage.getvalue()).decode('ascii')
