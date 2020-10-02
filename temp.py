# openpyxl 연습
# 뼈대 코드~!!
from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])
ws1.append(["1", "2", "3"])

wb.save(filename='articles.xlsx')