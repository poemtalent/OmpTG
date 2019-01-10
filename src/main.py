import os
import re as r #正则表达式库
import sys
from readalf import readalf
from getInit import getInitialHeader
from getFunc import getFunc
from Delete_Note import Delete_Note
from Function_declaration import getFunction_declaration
from Changejump import Changejump
from getBasicBlockSlice import getBasicBlockSlice
from Create_every_bb import Create_every_bb
from WCET_Generator import WCET_Output
try:
    Enter_File_Name=sys.argv[1]
except:
    print('Please Input ALF file u\'d like to analyze.\nAborted.')
    sys.exit(0)

WCETList={}

if os.path.isfile(Enter_File_Name) :
    hashtag_rule=r.compile(u'(\/\*(\s|.)*?\*\/)|(\/\/.*)')
    file = open(Enter_File_Name, 'r')
    content = file.readlines()
    head=getInitialHeader(content)  #head：alf代码总的函数声明
    file.close()
    #print(head)
    DATA=readalf(Enter_File_Name)#DATA：将代码保存为一个字符串
    #print(head)
    #print(DATA)
    list_func=getFunc(DATA)#将DATA里的每一个func提取出来组合为一个列表（含注释）
    Delete_Note(list_func)#将list_func的注释清除
    Every_func_mid_declaration=getFunction_declaration(list_func)
    filesname=[]
    for i in range(0,len(list_func)):
        list_func_temp=[]
        list_func_temp.append(list_func[i])
        dict_temp=getBasicBlockSlice(list_func_temp)
        #print(dict_temp)
        Changejump(dict_temp)
        #print(dict_temp)
        Create_every_bb(dict_temp,Every_func_mid_declaration,head,WCETList,filesname)
    WCET_Output(WCETList,os.path.splitext(Enter_File_Name)[0])
    print('Create ALF file Success!')
    # print(Every_func_mid_declaration)
    # print(list_func)
else:
    print('It\'s not a file')
