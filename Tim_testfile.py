import pandas as pd
from openpyxl import load_workbook

def writedata():
    # Initialize xlsx writer
    writer = pd.ExcelWriter('Tim_Test_data.xlsx', engine='xlsxwriter')
    workbook = writer.book

    df1 = pd.DataFrame({"A": [1,2,3],
                        "B": [1,2,3]})

    df1.to_excel(writer,
                sheet_name="sheet1",
                startrow=1,
                startcol=1)

    writer.save()

writedata()

