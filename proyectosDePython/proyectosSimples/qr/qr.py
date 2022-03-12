from matplotlib.pyplot import fill
import qrcode
link = 'https://factoraprendizaje.wordpress.com'
qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image()
img.save('QRLINK.png')