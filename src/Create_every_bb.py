# Create_every_bb
import os
import re as r #正则表达式库
import sys
from callFunction import GenerateCallFunction
from callFunction import findPosFromPoint
# dictio_bb={'return': '{ label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } }          { return }', 'bb_0': '{ label 64 { lref 64 "Circle::bb" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { dec_unsigned 32 0 } }    ', 'bb_1': '{ label 64 { lref 64 "Circle::bb::0:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }', 'bb1': '{ label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } }          { switch      { s_lt 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 100 } }      { target { dec_signed 1 { minus 1 } } { label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } } }      { default { label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } } }     }', 'bb2': '{ label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } }          { jump { label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } } leaving 0 }', 'bb3_0': '{ label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } with      { add 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 1 } { dec_unsigned 1 0 } }     }         ', 'bb3_1': '{ label 64 { lref 64 "Circle::bb3::1" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } } }    ', 'bb3_2': '{ label 64 { lref 64 "Circle::bb3::1:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }'}
# list1=[['{ alf', ' { macro_defs }', ' { least_addr_unit 8 }', ' little_endian', ' { exports', '  { frefs }', '  { lrefs '], {'f': ' { lref 64 "f" }', '_taskFunc0_': ' { lref 64 "_taskFunc0_" }', 'Circle': ' { lref 64 "Circle" }', '__original_main': ' { lref 64 "__original_main" }', '_taskFunc1_': ' { lref 64 "_taskFunc1_" }'}, ' }', ' }', ' { imports', '  { frefs', '   { fref 64 "$null" }', '   { fref 64 "$mem" }', '  }', '  { lrefs }', ' }', ' { decls }', ' { inits }', ' { funcs', '']
# dictio_decla={'Circle': '{ func   { label 64 { lref 64 "Circle" } { dec_unsigned 64 0 } }   { arg_decls }   { scope    { decls     { alloc 64 "%i.0" 32 }       { alloc 64 "%tmp4" 32 }      }    { inits }    { stmts          '}
def Create_every_bb (dic,dicti,li,WCETList,filesname):
    dictex={'a':1,'b':2}
    for bb in dic:
        if len(dic)!=1:
            if bb!='return':
                #Only have return statement
                getfunc_name=dic[bb]

                FuncLabel=findlabel(getfunc_name)
                FuncLabel=findlabel(getfunc_name)
                for i in range(0,len(filesname)):
                    if filesname[i] == FuncLabel.lower():
                        FuncLabel=FuncLabel+"_other"
                        # print("1")
                        break
                path='Generate_file/'+FuncLabel
                folder = os.path.exists(path)
                if not folder:
                    os.makedirs(path)
                # f = open('Generate_file/'+'Circle_'+bb+'.txt', 'w')
                GenerateFileName='Generate_file/'+FuncLabel+'/'+bb+'.alf'
                f = open(GenerateFileName, 'w')
                for i in range(0,len(li)):
                    #print(i)
                    if type(li[i]) is str:
                        f.write(li[i]+'\n')
                        #print(type(list[i]))
                    elif isinstance(li[i],dict):
                        t=dic[bb]
                        templabel=findlabel(t)
                        # print(templabel)
                        # temp=li[i][templabel]
                        temp=" { lref 64 \""+templabel+"\" }"
                        # print(temp)
                        f.write(temp)
                    else:
                        for j in range(0,len(li[i])):
                            f.write(li[i][j]+'\n')
                f.write(dicti[findlabel(getfunc_name)]+'\n')
                f.write(dic[bb]+'\n')
                call_body=find_call_body(dic[bb])
                if(call_body==0):
                    f.write(dic['return']+'\n')
                    for i in range(0,5):
                        for j in range(0,5-i):
                            f.write(' ')
                        f.write('}\n')
                else:
                    f.write(dic['return'] + '\n')
                    for i in range(0,3):
                        for j in range(0,3-i):
                            f.write(' ')
                        f.write('}\n')
                    f.write(GenerateCallFunction(call_body))
                    f.write('  }\n')
                    f.write(' }\n')
                f.close()
                WCET_Generator(FuncLabel,bb,GenerateFileName,WCETList)
        else:
            #Only have return statement
            getfunc_name=dic[bb]

            FuncLabel=findlabel(getfunc_name)
            FuncLabel=findlabel(getfunc_name)
            for i in range(0,len(filesname)):
                if filesname[i] == FuncLabel.lower():
                    FuncLabel=FuncLabel+"_other"
                    # print("1")
                    break
            path='Generate_file/'+FuncLabel
            folder = os.path.exists(path)
            if not folder:
                os.makedirs(path)
            # f = open('Generate_file/'+'Circle_'+bb+'.txt', 'w')

            GenerateFileName='Generate_file/'+FuncLabel+'/'+bb+'.alf'
            f = open(GenerateFileName, 'w')
            for i in range(0,len(li)):
                #print(i)
                if type(li[i]) is str:
                    f.write(li[i]+'\n')
                    #print(type(list[i]))
                elif isinstance(li[i],dict):
                    t=dic[bb]
                    templabel=findlabel(t)
                    temp=li[i][templabel]
                    f.write(temp)
                else:
                    for j in range(0,len(li[i])):
                        f.write(li[i][j]+'\n')
            f.write(dicti[findlabel(getfunc_name)]+'\n')
            f.write(dic[bb]+'\n')
            for i in range(0,5):
                for j in range(0,5-i):
                    f.write(' ')
                f.write('}\n')
            f.close()
            WCET_Generator(FuncLabel,bb,GenerateFileName,WCETList)
    funcname=findlabel(dic['return'])
    filesname.append(funcname.lower())


def findlabel(str):
    strex='"';
    stren=':';
    s_place=0;
    e_place=0;
    s_place=str.find(strex)
    e_place=str.find(stren,s_place+1)
    result = str[s_place+1:e_place]
    # while result[0]=="_":
    #     result=result[1:]
    # for i in range(0,len(result)):
    #     if(result[i]=="_"):
    #         s_place=i
    #     else:
    #         break
    # result = result[s_place+1:]
    return result
# Create_every_bb (dictio_bb,dictio_decla,list1)

def find_call_body(str):
    string=str.strip()
    start_call_place=string.find("call")
    if(start_call_place!=-1):
        #去掉label段
        strii=string[len(findPosFromPoint(string,0)):].strip()
        return strii
    else:
        return 0

def WCET_Generator(FuncName,BasicBlock,ALFile,WCETList):
    #call SWEET
    import subprocess
    std_hll=os.path.dirname(os.path.abspath(__file__))+'/Support/std_hll.alf'
    clt=os.path.dirname(os.path.abspath(__file__))+'/Support/CostTimeTable.clt'
    #ALF File=ALFile
    try:
        output = subprocess.Popen('sweet -i='+ALFile+','+std_hll+\
            ' -c extref=off -ae pu aac='+clt+' tc=st,op merge=all'\
                ,stdout=subprocess.PIPE,shell=True).communicate()
        WCET_Time=int(str(output[0]).split('table:')[-1].strip('\\n\"\ '))
        WCETList[FuncName+' '+BasicBlock]=WCET_Time
        print('WCET for '+FuncName+''+BasicBlock+'------'+str(WCET_Time))
    except:
        WCETList[FuncName+' '+BasicBlock]='ERROR'
        print('\n---'+FuncName+' '+BasicBlock+'---Output ERROR---\n')
