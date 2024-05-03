import pyhtml2pdf
from pyhtml2pdf import converter


def convert_html_to_pdf(source_html, output_filename):
    with open(source_html, "r") as html_file:
        html_content = html_file.read()
    # pdf_content = pyhtml2pdf.convert(html_content, output_filename)
    converter.convert(html_content, output_filename)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 1:
        print("Usage: python run_pyhtml2pdf.py")
        sys.exit(1)
    source_html = "index.html"
    output_pdf = "output_pyhtml2pdf.pdf"
    convert_html_to_pdf(source_html, output_pdf)
