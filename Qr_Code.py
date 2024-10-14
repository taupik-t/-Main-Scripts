import qrcode
from PIL import Image

def generate_qr_code(url, filename, size):
    qr = qrcode.QRCode(
        version=None,  # Let the library determine the best version for the given data
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Resize the image to the desired size
    img = img.resize((size, size), Image.Resampling.LANCZOS)

    img.save(filename)

if __name__ == "__main__":
    url = "https://uip3b-kalimantan.com/visitor_up2b-kaltim/registrasi/team"
    
    # url = "https://uip3b-kalimantan.com/visitor_up2b-kalsel/registrasi"
    # url = "https://uip3b-kalimantan.com/visitor_up2b-kaltim/registrasi/team"
    # url = "https://uip3b-kalimantan.com/visitor_up2b-kaltim/registrasi"
    # url = "https://uip3b-kalimantan.com/buku_tamu/registrasi/team"
    # url = "https://tamu.updkbarito.com/registrasi"

    filename = "QR_CODE UIP3B Kalselteng Tamu - Registrasi Team.png"
    # filename = "QR_CODE UIP3B Kalselteng Tamu - Registrasi.png"
    # filename = "QR_CODE UP2B Kaltimra Buku Tamu - Registrasi Team.png"
    # filename = "QR_CODE UP2B Kaltimra Buku Tamu - Registrasi.png"
    # filename = "QR_CODE UPDK Barito Buku Tamu - Registrasi.png"
    # filename = "QR_CODE UIP3B Buku Tamu - Registrasi Team.png"
    size = 2000  # 2K x 2K pixels

    generate_qr_code(url, filename, size)
    print(f"QR code image (2K x 2K) generated and saved as {filename}")
