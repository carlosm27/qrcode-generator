from django.shortcuts import render
import qrcode
import qrcode.image.svg
from .models import QrInfo
from io import BytesIO
from django.core.files.base import ContentFile

def qr_page(request):
    context = {}
    qr = {}
    if request.method == 'POST':
        factory = qrcode.image.svg.SvgImage
        qr_text =request.POST.get("qr_text", "")
        img = qrcode.make(qr_text,
                          image_factory=factory, box_size=20)
        stream= BytesIO()
        img.save(stream)
        qr_model = QrInfo(
            info= qr_text,
        )
        svg = stream.getvalue().decode()
        qr_model.image.save(f'{qr_model.date}.svg', ContentFile(svg))
        qr_model.save()
        context["svg"] = stream.getvalue().decode()
    return render(request, "qr_app/qr_bar.html", context)

def qrcode_generator(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("some_file.png")
    return img








