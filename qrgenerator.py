import qrcode
import os

data = input("enter the link: ").strip()
filename = input("name of the file: ").strip() + ".png"
qr = qrcode.QRCode(box_size=10, border=4)

qr.add_data(data)
qr.make(fit=True)  # this step is necessary

image = qr.make_image(fill_color='blue', back_color='white')

image.save(filename)

print("QR code generated:", filename)