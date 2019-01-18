import os
import re as r #正则表达式库
import sys,getopt
from help import ShowOptions
from readalf import readalf
from getInit import getInitialHeader
from getFunc import getFunc
from Delete_Note import Delete_Note
from Function_declaration import getFunction_declaration
from Changejump import Changejump
from getBasicBlockSlice import getBasicBlockSlice
from Create_every_bb import Create_every_bb
from WCET_Generator import WCET_Output



if __name__=="__main__":
    #Process Options
    File_Name=''
    WCET_File_Name=''
    Task_ALF_Output_Directiory=''
    getArgs={}
    options,args=getopt.getopt(sys.argv[1:],"hi:o:")
    for op,value in options:
        if op == '-h':
            ShowOptions()
            sys.exit(0)
        if op == '-i':
        	File_Name=value
        	continue
        if op == '-w':
        	WCET_File_Name=value
        	continue
        if op == '-t':
        	Task_ALF_Output_Directiory=value
    getArgs={'i':File_Name,'w':WCET_File_Name,'t':Task_ALF_Output_Directiory}
    print(getArgs)
    if (getArgs['w']!=''):
    	#w_Function
    	pass
    elif (getArgs['t']!=''):
    	#t_Function
    	pass
else:
    print("Please run this scripts directly.")