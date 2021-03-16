from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')

sheet = wb['Data']

def getvalue(x): return x.value

col_a = list(map(getvalue,sheet['A'][1:]))
col_b = list(map(getvalue,sheet['B'][1:]))
col_c = list(map(getvalue,sheet['C'][1:]))
col_d = list(map(getvalue,sheet['D'][1:]))
#print(col_a)
#print(col_b)
#print(col_c)
#print(col_d)

#pyplot.plot(col_a, col_b, label='Температура')
pyplot.plot(col_a, col_c, label='Отн.темп')
pyplot.plot(col_a, col_d, label='Активность')

pyplot.legend()
pyplot.show()