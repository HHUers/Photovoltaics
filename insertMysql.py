import pymysql
import time
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple


def insert_into_table(index, sql):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='photovoltaics')
    cursor = db.cursor()
    file = xlrd.open_workbook('data.xlsx')
    sheet = file.sheet_by_index(index)
    s_row = sheet.nrows
    s_col = sheet.ncols
    val = []
    for irow in range(1, s_row):
        list = []
        for icol in range(0, s_col):
            cell = sheet.cell_value(irow, icol)
            ctype = sheet.cell(irow, icol).ctype
            if icol == 0:
                list.append(int(cell))
            elif ctype == 3:  # 日期
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y-%m-%d')
                list.append(cell)
            elif cell =="":
                list.append(None)
            elif index == 3 and icol in range(8,11):
                list.append(round(cell,2))
            else:
                list.append(cell)
        val.append(list)
    print(val)
    try:
        cursor.executemany(sql, val)  # 如果发生错误则回滚
        db.commit()  # 提交到数据库执行
        print("提交成功")
    except Exception as ex:
        print(ex)
        db.rollback()  # 如果发生错误则回滚
    db.close()


if __name__ == '__main__':
    sql1 = "INSERT INTO web_projectoverview VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    sql2 = "INSERT INTO web_siteprofile VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql3 = "INSERT INTO web_temperature VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    sql4 = "INSERT INTO web_pvsystem VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    insert_into_table(0, sql1)
    time.sleep(2)
    insert_into_table(1, sql2)
    time.sleep(2)
    insert_into_table(2, sql3)
    time.sleep(2)
    insert_into_table(3, sql4)
