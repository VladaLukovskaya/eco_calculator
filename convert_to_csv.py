import csv
import os

from extract_text import extract_text_by_page


def export_as_csv(pdf_path, csv_path):
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        common_list = extract_text_by_page(pdf_path)
        for elem in common_list:
            for new_elem in elem:
                writer.writerow(new_elem)



if __name__ == '__main__':
    pdf_path = 'Fkko2019.pdf'
    csv_path = 'Fkko2019.csv'
    export_as_csv(pdf_path, csv_path)
