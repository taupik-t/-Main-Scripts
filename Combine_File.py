import PyPDF2


def combine_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()

    try :
        for pdf in input_pdfs:
            pdf_merger.append(pdf)

        with open(output_pdf, "wb") as merged_pdf:
            pdf_merger.write(merged_pdf)

        print(f"PDFs successfully combined into {output_pdf}")
    
    except Exception as e :
        print(f"Error: {e}")


if __name__ == "__main__":
    input_files = ["1.pdf", "2.pdf", "3.pdf", "4.pdf", "5.pdf", "6.pdf", "7.pdf", "8.pdf"]
    output_file = "Erlang Andriyanputra.pdf"
    combine_pdfs(input_files, output_file)
