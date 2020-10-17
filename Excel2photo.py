import xlrd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = xlrd.open_workbook('name.xlsx')
table = data.sheets()[0]

def plus4(ylist):
    ylist = np.array(ylist)+0.04
    return ylist

def plus2(ylist):
    ylist = np.array(ylist)+0.02
    return ylist

def minus2(ylist):
    ylist = np.array(ylist)-0.02
    return ylist

def minus4(ylist):
    ylist = np.array(ylist)-0.04
    return ylist

t1 = table.col_values(0)
x5 = t1[1:602]

t2 = table.col_values(1)
y5 = t2[1:602]
y5 = plus4(y5)


t4 = table.col_values(3)
x6 = t4[1:602]

t5 = table.col_values(4)
y6 = t5[1:602]
y6 = plus2(y6)

t7 = table.col_values(6)
x7 = t7[1:602]

t8 = table.col_values(7)
y7 = t8[1:602]


t10 = table.col_values(9)
x8 = t10[1:602]

t11 = table.col_values(10)
y8 = t11[1:602]
y8 = minus2(y8)
#红砂岩组，大理石数据不全
t13 = table.col_values(12)
x9 = t10[1:602]

t14 = table.col_values(13)
y9 = t11[1:602]
y9 = minus4(y9)

plt.plot(x5, y5, 'ko-',label=u"5cm源距",linewidth=1)
plt.plot(x6, y6, 'b,-',label=u"6cm源距",linewidth=1)
plt.plot(x7, y7, 'g^-',label=u"7cm源距",linewidth=1)
plt.plot(x8, y8, 'rs-',label=u"8cm源距",linewidth=1)
plt.plot(x9, y9, 'y*-',label=u"9cm源距",linewidth=1)
plt.title(u"红砂岩不同源距下波形对比图")

# plt.plot(x5, y5, 'b,-',label=u"6cm源距",linewidth=1)
# plt.plot(x6, y6, 'g^-',label=u"7cm源距",linewidth=1)
# plt.plot(x7, y7, 'rs-',label=u"8cm源距",linewidth=1)
# plt.plot(x8, y8, 'y*-',label=u"9cm源距",linewidth=1)
# plt.title(u"大理石不同源距下波形对比图")

plt.legend()
plt.xlabel(u"{}".format(table.cell(0,0).value))
plt.ylabel(u"{}".format(table.cell(0,1).value))
plt.show()
