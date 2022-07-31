import qrcode
import image                        
qr = qrcode.QRCode(
    version= 15,   # 15 mean high the no.bigger the code image and complicated picture
    box_size= 10,   # size of the box where qr code will be displayed
    border= 5   # It is white part of image -- border in all 4 sides with white color
    )
data = "https://www.canva.com/design/DAFHr07ZAm4/Ub0WuMWSHUpgcScSmkULbw/edit#"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill ="black",back_color="white")
img.save("test.png")