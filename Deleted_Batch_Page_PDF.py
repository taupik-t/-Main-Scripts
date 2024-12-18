import PyPDF2


def delete_pages(pdf_path, pages_to_delete):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page in range(len(pdf_reader.pages)):
            if page + 1 not in pages_to_delete:
                pdf_writer.add_page(pdf_reader.pages[page])

        with open("output.pdf", "wb") as output_file:
            pdf_writer.write(output_file)


if __name__ == "__main__":
    # Replace 'input.pdf' with you file names
    pdf_path = "input.pdf"

    # Replace or Add number of the page you wanted to deleted
    pages_to_delete = [2]
    
    # 
    delete_pages(pdf_path, pages_to_delete)
