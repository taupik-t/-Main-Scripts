import PyPDF2

def remove_pages(input_pdf_path, output_pdf_path, pages_to_remove):
    try:
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
                
        print("PDF processing complete. The pages have been removed successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_pdf_path}' was not found.")
    except PyPDF2.PdfReaderError:
        print("Error: There was an issue reading the PDF file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_pdf = 'output4.pdf'
output_pdf = 'output8.pdf'
pages_to_remove = [1, 2, 3]  # Pages to remove (0-based index)

remove_pages(input_pdf, output_pdf, pages_to_remove)
