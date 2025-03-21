import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def create_qr_code(data, file_path):
    img = qrcode.make(data)
    img.save(file_path)
    print(f"QR code saved to {file_path}")

def decode_qr_code(file_path):
    img = Image.open(file_path)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        print(f"Decoded data: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    data = "Never lose your permanent smile for temporary problems"
    qr_file_path = "C:/Users/DANISH LAPTOP/Documents/Python-Course/Class-Projects/assignment-04/Assignments_01/QR_code_encoder/newqrcode.png"
    create_qr_code(data, qr_file_path)
    decode_qr_code(qr_file_path)