#!/usr/bin/env python
# coding: utf-8
def findPosFromPoint(string,startPoint):
    FindText=''
    point=startPoint
    cnt=0
    flag=False #找到了
    while True:
        if(point>=len(string)):
            break
        if(flag==True):
            if(string[point]=='{'):
                cnt=cnt+1
            elif(string[point]=='}'):
                cnt=cnt-1
            FindText=FindText+string[point]
            #print(string[point])
            if (cnt==0):
                break
        else:
            #还没到
            if(string[point]=='{'):
                flag=True
                cnt=cnt+1
                FindText=FindText+string[point]
        point=point+1
    return FindText

def parseArgument(argument,num):
    #去括号
    argm=argument[1:-1].strip()
    argList=argm.split(' ')
    #print(argList)
    try:
        for word in argList[0]:
            if argList[0].isdigit():
                return ''
            elif argList[0]=='select':
                return parseArgument(findPosFromPoint(argm,0),num)
                #pass
            elif argList[0].startswith('f_') or argList[0].endswith('_f') or argList[0].startswith('float'):
                #64
                return '{ alloc 64 "%argm_' + str(num) + '" 64 }\n'
                #pass
            elif argList[0]=='s_to_f':
                return  '{ alloc 64 "%argm_' + str(num) + '" 64 }\n'
                #pass
            elif (argList[1].isdigit()):
                #add u_mul
                return '{ alloc 64 "%argm_'+str(num)+'" '+argList[1]+' }\n'
            else:
                #ERROR
                return ''
    except:
        return ''

def parseArgumentString(argument_string):
    output=''
    string=argument_string
    cnt=0#给参数编号
    while (len(string)>0):
        string = string.strip()
        tmpStr=findPosFromPoint(string,0)
        #update string (delete tmpStr in string)
        string=string[string.find(tmpStr)+len(tmpStr):]
        #
        if(tmpStr==''):
            break
        #print(tmpStr)
        output=output+parseArgument(tmpStr,cnt)
        cnt=cnt+1
    return output


def parseReturn(ReturnStatement):
    output=''
    returnArg=ReturnStatement.strip()
    if (returnArg==''):
        return ''
    else:
        returnList=returnArg[1:-1].strip().split(' ')
        #now only support addr
        if (returnList[0]=='addr'):
            output=output+'{ dec_unsigned '+returnList[1]+' 0 }'
            return output
        else:
            return ''
    pass
    


def GenerateCallFunction(CallStatement):
    #print('\nFound Call Function\n'+CallStatement+'\n\n')
    call_label=findPosFromPoint(CallStatement,CallStatement.find('call')+len('call'))
    #argument start and end position
    argument_st_pos=CallStatement.find(call_label)+len(call_label)
    argument_ed_pos=CallStatement.find('result')

    argument_string=CallStatement[argument_st_pos:argument_ed_pos].strip()

    output=parseArgumentString(argument_string)

    return_string=parseReturn(findPosFromPoint(CallStatement,CallStatement.find('result')+len('result')))
    FinalOutput='{ func'+ call_label+'{ arg_decls \n'+output+'} \
       { scope{ decls }{ inits }{ stmts{ label 64 { lref 64 "callfunction::bb" } \
       { dec_unsigned 64 0 } }    { return '+return_string+' }    }}}'
    return FinalOutput



#teststr='{ call { label 64 { lref 64 "callfunction" } { dec_unsigned 64 0 } } { add 64 { load 64 { addr 64 { fref 64 "%tmp27" } { dec_unsigned 64 0 } } } { select 128 0 63 { u_mul 64 64 { s_ext 32 64 { load 32 { addr 64 { fref 64 "%tmp28" } { dec_unsigned 64 0 } } } } { dec_unsigned 64 16 } } } { dec_unsigned 1 0 } } { add 64 { load 64 { addr 64 { fref 64 "%tmp31" } { dec_unsigned 64 0 } } } { select 128 0 63 { u_mul 64 64 { s_ext 32 64 { load 32 { addr 64 { fref 64 "%tmp32" } { dec_unsigned 64 0 } } } } { dec_unsigned 64 16 } } } { dec_unsigned 1 0 } } { load 64 { addr 64 { fref 64 "%tmp35" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp36" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp37" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp38" } { dec_unsigned 64 0 } } } { select 64 0 31 { u_mul 32 32 { load 32 { addr 64 { fref 64 "%tmp39" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp40" } { dec_unsigned 64 0 } } } } } { select 64 0 31 { u_mul 32 32 { load 32 { addr 64 { fref 64 "%tmp42" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp43" } { dec_unsigned 64 0 } } } } } result }'
#print(GenerateCallFunction(teststr))

