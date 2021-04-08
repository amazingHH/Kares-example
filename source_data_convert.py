import xlrd
import os
import xlwt
import xlsxwriter
from math import sqrt

def process():
    data = xlrd.open_workbook('data_source.xlsx')
    table = data.sheet_by_name('data1')
    nrow = table.nrows
    ncol=table.ncols
    print nrow,ncol
    
    workbook = xlsxwriter.Workbook('new_excel.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    for k in range(9):
        for i in range(10):
            for j in range (1000):
                worksheet.write(j+i*1000+k*10000, 0 , str(1000-i*100))
            #print(1000-i*100)
    for k in range(9):
        for i in range(10):
            for j in range(1000):
                worksheet.write(j+i*1000+k*10000, 1 , str(table.cell_value(j,i+1+k*10)))

    workbook.close()

def mse():
    target = [0.03,0.04,0.035,0.052,0.097]
    prediction = [0.03,0.04,0.04,0.05,0.1]
    error = []
    for i in range(len(target)):
        error.append(target[i] - prediction[i])
    print("Errors: ", error)
    print(error)
    squaredError = []
    absError = []
    for val in error:
        squaredError.append(val * val)
        absError.append(abs(val))
    print("Square Error: ", squaredError)
    print("Absolute Value of Error: ", absError)
    mse_value = sum(squaredError) / len(squaredError)
    rmse_value = sqrt(sum(squaredError) / len(squaredError))
    print("MSE = \n", mse_value)
    print("RMSE = \n", rmse_value)
    

if __name__ == "__main__": 
    process()
    #mse()
    
