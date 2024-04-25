from weasyprint import HTML

# Define your data
source_html = "index.html"
output_filename = "output_weasyprint.pdf"

# Main program
if __name__ == "__main__":
    HTML(source_html).write_pdf(output_filename)
