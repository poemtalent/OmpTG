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
                #argList[1],argList[2],argList[3]
                if(int(argList[3])-int(argList[2])+1>32):
                    return '{ alloc 64 "%argm_' + str(num) + '" 64 }\n'
                else:
                    return '{ alloc 64 "%argm_' + str(num) + '" 32 }\n'
                #pass
            elif argList[0].startswith('f') or argList[0].endswith('_f'):
                #64
                return '{ alloc 64 "%argm_' + str(num) + '" 64 }\n'
            elif argList[0].endswith('_ext'):
                #64
                return '{ alloc 64 "%argm_' + str(num) + '" 64 }\n'
                #pass
            elif argList[0]=='s_to_f':
                return  '{ alloc 64 "%argm_' + str(num) + '" 64 }\n'
            elif argList[0] == 'conc':
                if(int(argList[1])+int(argList[2])>32):
                    return '{ alloc 64 "%argm_' + str(num) + '" 64 }\n'
                else:
                    return '{ alloc 64 "%argm_' + str(num) + '" 32 }\n'
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

    while CallStatement[argument_ed_pos-1]=='%':
        #for %result
        argument_ed_pos = CallStatement.find('result',argument_ed_pos+1)

    argument_string=CallStatement[argument_st_pos:argument_ed_pos].strip()

    output=parseArgumentString(argument_string)

    return_string=parseReturn(findPosFromPoint(CallStatement,CallStatement.find('result')+len('result')))
    FinalOutput='{ func'+ call_label+'{ arg_decls \n'+output+'} \
       { scope{ decls }{ inits }{ stmts{ label 64 { lref 64 "callfunction::bb" } \
       { dec_unsigned 64 0 } }    { return '+return_string+' }    }}}'
    return FinalOutput


#Just For test
#teststr='{ call { label 64 { lref 64 "callfunction" } { dec_unsigned 64 0 } } { addr 64 { fref 64 "%result" } { dec_unsigned 64 0 } } { load 64 { addr 64 { fref 64 "%tmp1" } { dec_unsigned 64 0 } } } result }'
#print(GenerateCallFunction(teststr))

