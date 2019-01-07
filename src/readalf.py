import os
import re as r
def readalf(string):
    alfdata=''
    data_path=string#'mp_ompi.alf'
    data = open(data_path,'r')
    # body=open(data_path+ '.txt', 'w')
    line = data.readline()
    while line:             #直到读取完文件
         # body.write(line)
         if line[-1]!='\n':
              alfdata=alfdata+line
         else:
              alfdata=alfdata+line[:-1]
         line = data.readline()  #读取一行文件，包括换行符

    data.close()
    # body.close()
    return alfdata
# print(alfdata)
