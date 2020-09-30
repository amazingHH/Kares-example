__author__ = 'Administrator'
import os
import xlrd, xlsxwriter

dd = 0

def get_list():
    # 将文件读取出来放一个列表里面

    pwd = 'D:/code/metadata' # 获取文件目录
    source_xls = ["D:/code/metadata/1.xlsx", "D:/code/metadata/2.xlsx", "D:/code/metadata/3.xlsx", "D:/code/metadata/4.xlsx", "D:/code/metadata/5.xlsx",
                  "D:/code/metadata/6.xlsx", "D:/code/metadata/7.xlsx", "D:/code/metadata/8.xlsx", "D:/code/metadata/9.xlsx", "D:/code/metadata/10.xlsx",
                  "D:/code/metadata/11.xlsx", "D:/code/metadata/12.xlsx", "D:/code/metadata/13.xlsx", "D:/code/metadata/14.xlsx", "D:/code/metadata/15.xlsx",
                  "D:/code/metadata/16.xlsx", "D:/code/metadata/17.xlsx", "D:/code/metadata/18.xlsx", "D:/code/metadata/19.xlsx", "D:/code/metadata/20.xlsx",
                  "D:/code/metadata/21.xlsx", "D:/code/metadata/22.xlsx", "D:/code/metadata/23.xlsx", "D:/code/metadata/24.xlsx", "D:/code/metadata/25.xlsx",
                  "D:/code/metadata/26.xlsx", "D:/code/metadata/27.xlsx", "D:/code/metadata/28.xlsx", "D:/code/metadata/29.xlsx", "D:/code/metadata/30.xlsx",
                  "D:/code/metadata/31.xlsx", "D:/code/metadata/32.xlsx", "D:/code/metadata/33.xlsx", "D:/code/metadata/34.xlsx", "D:/code/metadata/35.xlsx",
                  "D:/code/metadata/36.xlsx", "D:/code/metadata/37.xlsx", "D:/code/metadata/38.xlsx", "D:/code/metadata/39.xlsx", "D:/code/metadata/40.xlsx",
                  "D:/code/metadata/41.xlsx", "D:/code/metadata/42.xlsx", "D:/code/metadata/43.xlsx", "D:/code/metadata/44.xlsx", "D:/code/metadata/45.xlsx",
                  "D:/code/metadata/46.xlsx", "D:/code/metadata/47.xlsx", "D:/code/metadata/48.xlsx", "D:/code/metadata/49.xlsx", "D:/code/metadata/50.xlsx",
                  "D:/code/metadata/51.xlsx", "D:/code/metadata/52.xlsx", "D:/code/metadata/53.xlsx", "D:/code/metadata/54.xlsx", "D:/code/metadata/55.xlsx",
                  "D:/code/metadata/56.xlsx", "D:/code/metadata/57.xlsx", "D:/code/metadata/58.xlsx", "D:/code/metadata/59.xlsx", "D:/code/metadata/60.xlsx",
                  "D:/code/metadata/61.xlsx", "D:/code/metadata/62.xlsx", "D:/code/metadata/63.xlsx", "D:/code/metadata/64.xlsx", "D:/code/metadata/65.xlsx",
                  "D:/code/metadata/66.xlsx", "D:/code/metadata/67.xlsx", "D:/code/metadata/68.xlsx", "D:/code/metadata/69.xlsx", "D:/code/metadata/70.xlsx",
                  "D:/code/metadata/71.xlsx", "D:/code/metadata/72.xlsx", "D:/code/metadata/73.xlsx", "D:/code/metadata/74.xlsx", "D:/code/metadata/75.xlsx",
                  "D:/code/metadata/76.xlsx", "D:/code/metadata/77.xlsx", "D:/code/metadata/78.xlsx", "D:/code/metadata/79.xlsx", "D:/code/metadata/80.xlsx",
                  "D:/code/metadata/81.xlsx", "D:/code/metadata/82.xlsx", "D:/code/metadata/83.xlsx", "D:/code/metadata/84.xlsx", "D:/code/metadata/85.xlsx",
                  "D:/code/metadata/86.xlsx", "D:/code/metadata/87.xlsx", "D:/code/metadata/88.xlsx", "D:/code/metadata/89.xlsx", "D:/code/metadata/90.xlsx",
                  "D:/code/metadata/91.xlsx", "D:/code/metadata/92.xlsx", "D:/code/metadata/93.xlsx", "D:/code/metadata/94.xlsx", "D:/code/metadata/95.xlsx",
                  "D:/code/metadata/96.xlsx", "D:/code/metadata/97.xlsx", "D:/code/metadata/98.xlsx", "D:/code/metadata/99.xlsx", "D:/code/metadata/100.xlsx",]
    target_xls = "D:/code/final.xlsx"
    # 读取数据
    data = []
    arr = [[0]*6000 for _ in range(100)]
    for i in range(len(source_xls)):
        wb = xlrd.open_workbook(source_xls[i])
        sheet = wb.sheet_by_index(0)
        for rownum in range(sheet.nrows):
            data.append(sheet.row_values(rownum))
            #print(sheet.row_values(rownum))
            #arr[i].append(sheet.row_values(rownum))
            arr[i][rownum] = sheet.cell_value(rownum,0)
            print(arr[i][rownum])
    #print(arr)
    # 写入数据
    workbook = xlsxwriter.Workbook(target_xls)
    worksheet = workbook.add_worksheet()
    #font = workbook.add_format({"font_size":14})
    for i in range(100):
        for j in range(6000):
            #print(arr[i][j])
            worksheet.write(i, j, arr[i][j])
    # 关闭文件流
    workbook.close()


if __name__ == '__main__':
    get_list()