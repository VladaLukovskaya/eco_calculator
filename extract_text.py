import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from edit_text import find_all


def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True, maxpages=10):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            dict = find_all(text)
            yield dict
            # yield text

            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        dict = find_all(page)
        # print(page)
        # print()
        return dict


if __name__ == '__main__':
   print(extract_text('Fkko2019.pdf'))
