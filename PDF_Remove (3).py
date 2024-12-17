import PyPDF2

def remove_pages(input_pdf_path, output_pdf_path, pages_to_remove):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        writer = PyPDF2.PdfWriter()

        # Iterate through all the pages and add those not in the removal list
        for page_num in range(len(reader.pages)):
            if page_num not in pages_to_remove:
                writer.add_page(reader.pages[page_num])

        # Write the output PDF file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

# Example usage
input_pdf = 'DOKUMEN LKS NASIONAL 2024 (Surat Izin Orang Tua).pdf'
output_pdf = 'output1.pdf'
pages_to_remove = [1]  # Pages to remove (0-based index)

remove_pages(input_pdf, output_pdf, pages_to_remove)
