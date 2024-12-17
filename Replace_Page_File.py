import PyPDF2


def replace_first_page(input1_path, input2_path, output_path):
    # Open the PDF files in binary mode
    with open(input1_path, "rb") as input1_file, open(input2_path, "rb") as input2_file:
        # Create PDF readers for both input files
        input1_reader = PyPDF2.PdfReader(input1_file)
        input2_reader = PyPDF2.PdfReader(input2_file)

        # Create a PDF writer for the output file
        output_writer = PyPDF2.PdfWriter()

        # Add the first page of input1 to the output
        output_writer.add_page(input1_reader.pages[0])

        # Add the remaining pages of input2 to the output
        for page_num in range(1, len(input2_reader.pages)):
            output_writer.add_page(input2_reader.pages[page_num])

        # Write the output to a new PDF file
        with open(output_path, "wb") as output_file:
            output_writer.write(output_file)


if __name__ == "__main__":
    input1_path = "input1.pdf"
    input2_path = "input2.pdf"
    output_path = "output.pdf"

    replace_first_page(input1_path, input2_path, output_path)
    print(f"First page replaced and saved to {output_path}")
