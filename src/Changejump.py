# Changejump
import os
import re as r #正则表达式库
import sys
import operator
# dict={'return': '{ label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } }          { return }', 'bb': '{ label 64 { lref 64 "Circle::bb" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { dec_unsigned 32 0 } }     { label 64 { lref 64 "Circle::bb::0:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }', 'bb1': '{ label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } }          { switch      { s_lt 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 100 } }      { target { dec_signed 1 { minus 1 } } { label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } } }      { default { label 64 { lref 64 "Circle::bb5" } { dec_unsigned 64 0 } } }     }', 'bb2': '{ label 64 { lref 64 "Circle::bb2" } { dec_unsigned 64 0 } }          { jump { label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } } leaving 0 }', 'bb3': '{ label 64 { lref 64 "Circle::bb3" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } with      { add 32 { load 32 { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } } { dec_unsigned 32 1 } { dec_unsigned 1 0 } }     }          { label 64 { lref 64 "Circle::bb3::1" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%i.0" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%tmp4" } { dec_unsigned 64 0 } } } }     { label 64 { lref 64 "Circle::bb3::1:::1" } { dec_unsigned 64 0 } }     { jump { label 64 { lref 64 "Circle::bb1" } { dec_unsigned 64 0 } } leaving 0 }'}
def Changejump (dict,filesname_sum,call_result,strr):
    if strr=='w':
        changedata = ''
        for bb in   dict.keys():

            if bb!='return':
                start = 'label'    #被匹配的字符串
                start_p=0
                end_p=0
                start_pl=0
                string=dict[bb]
                call_label_palce=0
                start_pl=string.find(start)
                #print(start_pl)
                start_place=string.find(start,start_pl+5)
                #print(start_place)
                prestart_place=0
                while start_place!=-1:
                    num = 2
                    for I in range(0, start_place):

                        if string[start_place - I] == "{":
                            num -= 1
                            if num == 0:
                                prestart_place = start_place - I
                                break
                    ss=string[prestart_place:start_place]
                    if (string[prestart_place:start_place].find("call") == -1):
                # while start_place != -1:
                #     if(string[start_place-8:start_place].find("call")==-1):

                        num=1
                        string=dict[bb]
                        for j in range(0,start_place):
                            #print(i)
                            if string[start_place-j]=='{':
                                start_p=start_place-j
                                break
                        for i in range(start_place,len(string)):
                            if string[i]=='{':
                                num+=1
                            elif string[i]=='}':
                                num-=1
                                if num==0:
                                    end_p=i
                                    num=1
                                    break
                        # try:
                        dict[bb]=dict[bb][:start_p]+changedata+dict[bb][end_p:]
                        start_place = dict[bb].find(start, end_p)
                        # except:
                        #     print("changejump"+dict[bb]
                    else:
                        string=dict[bb]
                        num=1
                        for i in range(0,start_place):
                            #print(i)
                            if string[start_place-i]=='{':
                                start_p=start_place-i
                                break
                        for i in range(start_place,len(string)):
                            if string[i]=='{':
                                num+=1
                            elif string[i]=='}':
                                num-=1
                                if num==0:
                                    end_p=i
                                    num=1
                                    break
                        strii=string[start_p:end_p]
                        call_start_palce=strii.find('"')
                        call_end_palce=strii.find('"',call_start_palce+1)
                        strii=strii[:call_start_palce+1]+"callfunction"+strii[call_end_palce:]
                        dict[bb]=dict[bb][:start_p]+strii+dict[bb][end_p:]
                        start_place=dict[bb].find(start,end_p)

                    # else:
                    #     print(string[call_label_palce:start_place])
                    #     call_label_palce=(string[call_label_palce:start_place].find("call")
                    #     labell = 'label'
                    #     call_label_palce=string.find(labell,call_label_palce)
                    #     call_end=string.find(labell,call_label_palce+1)
                    #     print(string[call_label_palce+1:call_end])
                    #     print("__________________________________________")
                    #     string = string[call_label_palce+1:]+"callfunction"+string[:call_end]
                    #     call_label_palce+=4
                    #     start_place=dict[bb].find(start,call_end)


            else:
                num=0
                start_pl=0
                end_pl=0
                string=dict[bb]
                for i in range(0,len(string)):
                    if string[i]=='{':
                        start_pl=i
                        break

                for i in range(0,len(string)):
                    if string[i]=='{':
                        num+=1
                    elif string[i]=='}':
                        num-=1
                        if num==0:
                            end_pl=i
                            break
                changedata=dict['return'][start_pl:end_pl]
    elif strr=='b':    #记录task中call的函数名
        for bb in dict.keys():
            call_func_temp=[]
            call_func_tempp=[]
            call_func={}  #返回的函数名列表
            func = dict[bb]  #这个taskfunc的主题
            findcallname(func, call_func,call_func_tempp,filesname_sum,call_result)
            for i in call_func.keys():
                call_func_temp.append(call_func[i])
            while operator.eq(call_func_temp,call_func_tempp)==False:
                call_func_tempp=call_func_temp
                for i in call_func_temp:
                    findcallname(filesname_sum[i], call_func, call_func_tempp,filesname_sum,call_result)
                call_func_temp=[]
                for i in call_func.keys():
                    call_func_temp.append(call_func[i])
        asd='sd'
        return call_func
def findcallname(body,call_name,temp,real_call,call_result):
    call_name_st = body.find('call')
    tempp=[]
    tempp=tempp+temp
    while call_name_st != -1:
        if (body[call_name_st - 1] == ' ' or body[call_name_st - 1] == '{') and (body[call_name_st + 4] == ' ' or body[call_name_st + 4] == '{'):
            call_name_st = body.find('"', call_name_st)
            call_name_en = body.find('"', call_name_st + 1)
            for i in range(0,call_name_st):
                if body[call_name_st-1-i]=='"':
                    stcall_st=call_name_st-1-i
                    break
            for i in range(0, stcall_st):
                if body[stcall_st-1 - i] == '"':
                    stcall_en = stcall_st-1 - i
                    break
            a=body[stcall_en + 1:stcall_st]
            call_result[a] = body[call_name_st + 1:call_name_en]
            if (body[call_name_st + 1:call_name_en] not in tempp) and(body[call_name_st + 1:call_name_en] in real_call.keys()):
                call_name[a]=body[call_name_st + 1:call_name_en]
                tempp.append(body[call_name_st + 1:call_name_en])
            # call_name.append(body[call_name_st + 1:call_name_en])
            call_name_st = body.find('call', call_name_en)




    #
# Changejump (dict)
# print(dict)

def findlabel(str):
    strex = '"';
    stren = ':';
    s_place = 0;
    e_place = 0;
    s_place = str.find(strex)
    e_place = str.find(stren, s_place + 1)
    result = str[s_place + 1:e_place]

    return result