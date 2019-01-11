import xlwt
if _name_ =="_main_":
	book = xlwt.Workbook(encoding='utf-8',
	                     style_compression=0)
	sheet=book.add_sheet('deed')
	sheet.write(0, 0, 'hstrdadf ')
	sheet.write(1, 1, '中午'.endswith('utf-8'))
	book.save('d:\\11.xls')
