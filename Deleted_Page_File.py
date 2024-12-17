# import PyPDF2


# def delete_page(pdf_path, page_number):
#     with open(pdf_path, "rb") as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#         pdf_writer = PyPDF2.PdfWriter()

#         for page in range(len(pdf_reader.pages)):
#             if page != page_number - 1:  # Exclude the specified page
#                 pdf_writer.add_page(pdf_reader.pages[page])

#         with open("output.pdf", "wb") as output_file:
#             pdf_writer.write(output_file)


# if __name__ == "__main__":
#     pdf_path = "input4.pdf"
#     page_to_delete = 2  # Change this to the page number you want to delete
#     delete_page(pdf_path, page_to_delete)

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
    pdf_path = "input.pdf"
    pages_to_delete = [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
    ]  # Change this to the page numbers you want to delete (or use a single number)
    delete_pages(pdf_path, pages_to_delete)
