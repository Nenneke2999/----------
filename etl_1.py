import openpyxl
import psycopg2
from openpyxl.utils.exceptions import InvalidFileException
import sys

if len(sys.argv) < 2:
    
    print('Please provide filename')
    exit()

try:
    workbook = openpyxl.load_workbook(sys.argv[1], data_only=True)
    worksheets = workbook.get_sheet_names()

except InvalidFileException:
    print('Error opening file')
    exit()

conn = psycopg2.connect(
    port = 5433,
    dbname="educational_practice",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""CREATE TABLE if not exists public.overdue
            (subj_RF varchar,
             MO varchar,
             INN varchar,
             status varchar,
             exit_type varchar,
             GTIN varchar,
             ref varchar,
             dose_per_pack int,
             pack int,
             dose int,
             expir_date date,
             days_overdue int)""")

for sheet in worksheets:
    for row in workbook[sheet].iter_rows(min_row=3, values_only=True):
        cur.execute("""INSERT INTO public.overdue (subj_RF, MO, INN, status, exit_type, GTIN, ref, dose_per_pack, pack, dose, expir_date, days_overdue) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", row[:12])

conn.commit()
cur.close()
conn.close()