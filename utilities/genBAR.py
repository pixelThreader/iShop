from io import BytesIO
from barcode import EAN13
from barcode.writer import ImageWriter


def bar(number, name):
    rv = BytesIO()
    EAN13(str(100000000000), writer=ImageWriter()).write(rv)
    with open(
        "E:/Projects/iShop/static/Uploads_from_User/barRetail/iS" + name + ".jpeg", "wb"
    ) as f:
        EAN13(str(number), writer=ImageWriter()).write(f)
    return
