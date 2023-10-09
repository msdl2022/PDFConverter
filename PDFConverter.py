import tabula
import pandas as pd

# Specify the PDF file you want to convert
pdf_file = "example.pdf"

# Use tabula to extract tables from the PDF
# You may need to adjust the `pages` parameter to specify which page(s) to extract
tables = tabula.read_pdf(pdf_file, pages='all')

# Combine the extracted tables into a single DataFrame
# If you have multiple tables, you may need to loop through `tables`
# and concatenate them accordingly
df = pd.concat(tables)

# Specify the output Excel file
excel_file = "output.xlsx"

# Save the DataFrame to an Excel file
df.to_excel(excel_file, index=False)

print(f"Data from {pdf_file} has been successfully converted to {excel_file}.")
