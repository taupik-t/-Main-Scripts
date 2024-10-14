# from PIL import Image
# import numpy as np
# import cv2

# def remove_white_background(input_image_path, output_image_path):
#     # Open the input image
#     img = Image.open(input_image_path).convert("RGBA")
#     img_np = np.array(img)

#     # Convert RGBA to BGR
#     img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGBA2BGR)
#     # Convert to grayscale
#     gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
#     # Create a binary mask where white is 255 and everything else is 0
#     _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

#     # Create a mask for the alpha channel
#     alpha = cv2.GaussianBlur(mask, (5, 5), 0)
#     alpha = cv2.merge([alpha, alpha, alpha])

#     # Use the mask to apply transparency to the original image
#     img_bgra = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2BGRA)
#     img_bgra[:, :, 3] = alpha[:, :, 0]

#     # Convert back to PIL Image and save
#     img_out = Image.fromarray(cv2.cvtColor(img_bgra, cv2.COLOR_BGRA2RGBA))
#     img_out.save(output_image_path)

# if __name__ == "__main__":
#     input_image_path = "qr_code_hd.png"  # Replace with your input image path
#     output_image_path = "output_image.png"  # Replace with your output image path

#     remove_white_background(input_image_path, output_image_path)
#     print(f"Processed image saved as {output_image_path}")
from PIL import Image

def remove_white_background(input_image_path, output_image_path):
    # Open the input image
    img = Image.open(input_image_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Change all white (also shades of whites)
        # pixels to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            # Change to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_image_path, "PNG")

if __name__ == "__main__":
    input_image_path = "QR_CODE UIP3B Kalselteng Tamu - Registrasi Team.png"
    output_image_path = "QR_CODE UIP3B Kalselteng Tamu - Registrasi Team (No Background).png"
    remove_white_background(input_image_path, output_image_path)
    print(f"Processed image saved as {output_image_path}")

    input_image_path = "QR_CODE UIP3B Kalselteng Tamu - Registrasi.png"
    output_image_path = "QR_CODE UIP3B Kalselteng Tamu - Registrasi (No Background).png"
    remove_white_background(input_image_path, output_image_path)
    print(f"Processed image saved as {output_image_path}")

    input_image_path = "QR_CODE UP2B Kaltimra Buku Tamu - Registrasi Team.png"
    output_image_path = "QR_CODE UP2B Kaltimra Buku Tamu - Registrasi Team (No Background).png"
    remove_white_background(input_image_path, output_image_path)
    print(f"Processed image saved as {output_image_path}")

    input_image_path = "QR_CODE UP2B Kaltimra Buku Tamu - Registrasi.png"
    output_image_path = "QR_CODE UP2B Kaltimra Buku Tamu - Registrasi (No Background).png"
    remove_white_background(input_image_path, output_image_path)
    print(f"Processed image saved as {output_image_path}")

    input_image_path = "QR_CODE UPDK Barito Buku Tamu - Registrasi.png"
    output_image_path = "QR_CODE UPDK Barito Buku Tamu - Registrasi (No Background).png"
    remove_white_background(input_image_path, output_image_path)
    print(f"Processed image saved as {output_image_path}")

    input_image_path = "QR_CODE UIP3B Buku Tamu - Registrasi Team.png"
    output_image_path = "QR_CODE UIP3B Buku Tamu - Registrasi Team (No Background).png"
    remove_white_background(input_image_path, output_image_path)
    print(f"Processed image saved as {output_image_path}")
    