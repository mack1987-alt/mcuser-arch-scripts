import pyqrcode
from PIL import Image

print("Generate QR code")
link = input("Enter text/url: ")

qr_code = pyqrcode.create(link)
qr_code.png("/path/to/file/name.png", scale=5)
Image.open("/path/to/file/name.png")