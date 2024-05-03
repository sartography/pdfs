import pdfkit

# Define your data
source_html = "index.html"
output_filename = "output_pdfkit.pdf"

# Main program
if __name__ == "__main__":
    pdfkit.from_file(source_html, output_filename)
