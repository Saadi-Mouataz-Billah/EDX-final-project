from PIL import Image, ImageDraw, ImageFont
import qrcode
import json
import cv2

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

def qr_reader(qrcode):
    ...


def qr_validator():
    ...


def main():
    generate_qrcode("mouataz", "saadi", "123456789")

if __name__ == "__main__":
    main()