import qrcode
import io

def generar_qr(link,color1):

    qr = qrcode.QRCode(box_size=10, border=2)

    qr.add_data(link)


    imagen = qr.make_image(fill_color=color1, background="white")


    imagen_byte = io.BytesIO()
    imagen.save(imagen_byte, format = "png")
    imagen_byte = imagen_byte.getvalue()

    return imagen_byte