import qrcode

data = input('Enter some text or URL').strip()  #strip() is to get rid of white space after user type
file_name = input('Enter the file name:').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')

image.save(file_name)

print(f'Qrcode is saved as {file_name} ')