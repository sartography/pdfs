from xhtml2pdf import pisa             # import python module

# Define your data
source_html = "index.html"
output_filename = "test.pdf"

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to receive result

    # close output file
    result_file.close()                 # close output file

    # return True on success and False on errors
    return pisa_status.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    with open(source_html, 'r') as f:
        source_html_content = f.read()
    convert_html_to_pdf(source_html_content, output_filename)
