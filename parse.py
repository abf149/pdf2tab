from tabula import read_pdf

def extract_tables_from_pdf(pdf_filename):
    # Use Tabula to extract tables from the PDF
    tables = read_pdf(pdf_filename, pages='all', multiple_tables=True)

    # Yield each table as a DataFrame
    for table in tables:
        yield table

# Usage
pdf_file = '2021 FULL _Research_Expenditures_by_Sponsor.pdf'
for i, df in enumerate(extract_tables_from_pdf(pdf_file)):
    # 'df' is a pandas DataFrame. You can process it as needed.
    # For example, you can print the DataFrame, analyze it, or save it to CSV.
    print(f"Table {i}:")
    print(df)

    # Optionally, save to CSV
    df.to_csv(f'output_table_{i}.csv', index=False)

