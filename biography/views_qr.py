# views_qr.py
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
import os

def qr_with_logo(request):
    url = "https://torobaevergeshbio.onrender.com"  # Сенин сайтың
    logo_path = os.path.join(settings.STATIC_ROOT, 'images', 'logo.png')  # логотипти статиктен алабыз

    # QR код түзүү
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Логотип кошуу
    if os.path.exists(logo_path):
        from PIL import Image
        logo = Image.open(logo_path)

        # Логотиптин өлчөмүн тууралоо
        basewidth = int(img_qr.size[0] / 4)  # QR коддун 1/4 бөлүгүн ээлейт
        wpercent = (basewidth / float(logo.size[0]))
        hsize = int((float(logo.size[1]) * float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

        # QR коддун ортосуна жайгаштыруу
        pos = ((img_qr.size[0] - logo.size[0]) // 2, (img_qr.size[1] - logo.size[1]) // 2)
        img_qr.paste(logo, pos)

    # Сүрөттү браузерге жөнөтүү
    buffer = BytesIO()
    img_qr.save(buffer, "PNG")
    buffer.seek(0)
    return HttpResponse(buffer, content_type="image/png")
