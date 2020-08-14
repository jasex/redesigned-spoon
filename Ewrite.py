import xlwt


def writeExcel(list):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('test')
    row=len(list)
    # 写入excel
    # 参数对应 行, 列, 值
    for i in range(row):
        stu=list[i]
        col=len(stu)
        for j in range(col):
            worksheet.write(i,j,stu[j])
    # 保存
    workbook.save('Excel_test.xls')
    
