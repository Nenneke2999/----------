import asyncpg
import config
import xlsxwriter
import io
from aiogram.types import BufferedInputFile

async def report():
    conn = await asyncpg.connect(user=config.USER, password = config.PASSWORD, database = config.DATABASE, host = config.HOST)
    rows = await conn.fetch('SELECT subj_RF, SUM(dose), ROUND(AVG(days_overdue)) FROM public.overdue GROUP BY subj_rf')
    wb = await convert(rows)
    await conn.close()
    return wb

async def convert(rows):
    output = io.BytesIO()
    wb = xlsxwriter.Workbook(output, {'in_memory': True})
    ws = wb.add_worksheet()
    ws.write(0, 0, 'Субъект РФ')
    ws.write(0, 1, 'Количество доз')
    ws.write(0, 2, 'Просрочено дней')
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            ws.write(i+1, j, rows[i][j])
    wb.close()
    output.seek(0)
    return BufferedInputFile(output.read(), filename='report.xlsx')