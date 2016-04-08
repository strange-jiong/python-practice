__author__ = 'jiong'
import xlwt

with open('city.txt') as f:
    content = f.read()
    dic = eval(content)

file = xlwt.Workbook()
table = file.add_sheet("Test", cell_overwrite_ok=True)

for k, v in dic.items():
    table.write(int(k) - 1, 0, k)
    # 解码得和txt的编码一致
    table.write(int(k) - 1, 1, str(v).decode('utf-8'))

file.save('result.xls')
