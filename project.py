from PIL import Image, ImageDraw, ImageFont
import qrcode
# import ... from ...
# import ... from ...

def generate_qrcode(name, fname, sid):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    data = f"{name}-{fname}-{sid}"
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'{data}.png')
    print("qr code generated", qr)

def main():
    generate_qrcode("mouataz", "saadi", "123456789")

if __name__ == "__main__":
    main()