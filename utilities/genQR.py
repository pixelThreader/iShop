import qrcode
import os
def qr(name, textfile):
    x = open(textfile).read()
    img = qrcode.make(x)
    type(img)
    img.save(os.path.join("D:/Django/iShop/static/Uploads_from_User/qrRetail/iS" + name + ".png"))
    return "Saved"