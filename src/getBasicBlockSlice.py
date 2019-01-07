# getBasicBlockSlice
import os
import re as r #正则表达式库
import sys
# li=['{ func   { label 64 { lref 64 "_taskFunc34_" } { dec_unsigned 64 0 } }   { arg_decls    { alloc 64 "%__arg" 64 }   }   { scope    { decls     { alloc 64 "%tmp" 64 }       { alloc 64 "%_tenv" 64 }       { alloc 64 "%m" 32 }       { alloc 64 "%in" 64 }       { alloc 64 "%out" 64 }       { alloc 64 "%W" 64 }       { alloc 64 "%nW" 32 }       { alloc 64 "%n" 32 }       { alloc 64 "%tmp1" 64 }       { alloc 64 "%tmp3" 64 }       { alloc 64 "%tmp5" 32 }       { alloc 64 "%tmp6" 64 }       { alloc 64 "%tmp8" 64 }       { alloc 64 "%tmp9" 64 }       { alloc 64 "%tmp11" 64 }       { alloc 64 "%tmp12" 64 }       { alloc 64 "%tmp14" 64 }       { alloc 64 "%tmp15" 64 }       { alloc 64 "%tmp17" 32 }       { alloc 64 "%tmp18" 64 }       { alloc 64 "%tmp20" 32 }       { alloc 64 "%tmp21" 32 }       { alloc 64 "%tmp22" 64 }       { alloc 64 "%tmp23" 64 }       { alloc 64 "%tmp24" 64 }       { alloc 64 "%tmp25" 32 }       { alloc 64 "%tmp26" 32 }       { alloc 64 "%tmp27" 32 }       { alloc 64 "%tmp29" 32 }       { alloc 64 "%tmp31" 64 }      }    { inits }    { stmts          { label 64 { lref 64 "_taskFunc34_::bb" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%tmp" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%__arg" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::11" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp1" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%tmp" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::13" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%tmp1" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::15" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp3" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::17" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp5" } { dec_unsigned 64 0 } } with      { load 32 { load 64 { addr 64 { fref 64 "%tmp3" } { dec_unsigned 64 0 } } } }     }          { label 64 { lref 64 "_taskFunc34_::bb::18" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%m" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%tmp5" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::20" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp6" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::22" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp8" } { dec_unsigned 64 0 } } with      { load 64       { add 64 { load 64 { addr 64 { fref 64 "%tmp6" } { dec_unsigned 64 0 } } } { dec_unsigned 64 8 } { dec_unsigned 1 0 } }      }     }          { label 64 { lref 64 "_taskFunc34_::bb::23" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%in" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%tmp8" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::25" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp9" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::27" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp11" } { dec_unsigned 64 0 } } with      { load 64       { add 64 { load 64 { addr 64 { fref 64 "%tmp9" } { dec_unsigned 64 0 } } } { dec_unsigned 64 16 } { dec_unsigned 1 0 } }      }     }          { label 64 { lref 64 "_taskFunc34_::bb::28" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%out" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%tmp11" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::30" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp12" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::32" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp14" } { dec_unsigned 64 0 } } with      { load 64       { add 64 { load 64 { addr 64 { fref 64 "%tmp12" } { dec_unsigned 64 0 } } } { dec_unsigned 64 24 } { dec_unsigned 1 0 } }      }     }          { label 64 { lref 64 "_taskFunc34_::bb::33" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%W" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%tmp14" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::35" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp15" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::37" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp17" } { dec_unsigned 64 0 } } with      { load 32       { add 64 { load 64 { addr 64 { fref 64 "%tmp15" } { dec_unsigned 64 0 } } } { dec_unsigned 64 32 } { dec_unsigned 1 0 } }      }     }          { label 64 { lref 64 "_taskFunc34_::bb::38" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%nW" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%tmp17" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::40" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp18" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::42" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp20" } { dec_unsigned 64 0 } } with      { load 32       { add 64 { load 64 { addr 64 { fref 64 "%tmp18" } { dec_unsigned 64 0 } } } { dec_unsigned 64 36 } { dec_unsigned 1 0 } }      }     }          { label 64 { lref 64 "_taskFunc34_::bb::43" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%n" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%tmp20" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::44" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp21" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%m" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::45" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp22" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%in" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::46" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp23" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%out" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::47" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp24" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%W" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::48" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp25" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%nW" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::49" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp26" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%nW" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::50" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp27" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%n" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::52" } { dec_unsigned 64 0 } }     { store { addr 64 { fref 64 "%tmp29" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%m" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb::53" } { dec_unsigned 64 0 } }     { call { label 64 { lref 64 "fft_twiddle_4" } { dec_unsigned 64 0 } } { dec_unsigned 32 0 } { load 32 { addr 64 { fref 64 "%tmp21" } { dec_unsigned 64 0 } } } { load 64 { addr 64 { fref 64 "%tmp22" } { dec_unsigned 64 0 } } } { load 64 { addr 64 { fref 64 "%tmp23" } { dec_unsigned 64 0 } } } { load 64 { addr 64 { fref 64 "%tmp24" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp25" } { dec_unsigned 64 0 } } }      { s_div 32 32 { load 32 { addr 64 { fref 64 "%tmp26" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp27" } { dec_unsigned 64 0 } } } }      { load 32 { addr 64 { fref 64 "%tmp29" } { dec_unsigned 64 0 } } }      result     }          { label 64 { lref 64 "_taskFunc34_::bb::54" } { dec_unsigned 64 0 } }     { jump      { label 64 { lref 64 "_taskFunc34_::bb30" } { dec_unsigned 64 0 } }      leaving      0     }          { label 64 { lref 64 "_taskFunc34_::bb30" } { dec_unsigned 64 0 } }          { store { addr 64 { fref 64 "%tmp31" } { dec_unsigned 64 0 } } with { load 64 { addr 64 { fref 64 "%_tenv" } { dec_unsigned 64 0 } } } }          { label 64 { lref 64 "_taskFunc34_::bb30::2" } { dec_unsigned 64 0 } }     { call { label 64 { lref 64 "ort_taskenv_free" } { dec_unsigned 64 0 } } { load 64 { addr 64 { fref 64 "%tmp31" } { dec_unsigned 64 0 } } } { label 64 { lref 64 "_taskFunc34_" } { dec_unsigned 64 0 } } result }          { label 64 { lref 64 "_taskFunc34_::bb30::3" } { dec_unsigned 64 0 } }     { return { addr 64 { fref 64 "$null" } { dec_unsigned 64 0 } } }    }   }  }']


def getBasicBlockSlice(list):
        '''
        负责人：覃辉，苏文辉
        目的：将大BB转为一个个小BB，存成一个list
        ( 碰到label元素，将label修改成returnBB对应的label，所以return的label段需要在list中特殊标明，方便易找)
        # return 要求：切出list对应的大BB的每一个小BB（按每个label为元素），按上述要求改进元素，并将这些元素组成一个list，返回。

        未完成，bug已经清除，还差跳转功能
        '''
        count=1
        for bb in list:
            dict = {}  # 创建字典
            start_flag = 'return'
            return_start_place = bb.find(start_flag)
            s=bb[:return_start_place-1]
            s1=s[::-1]
            return_start_pl=s1.find('lebal')
            for j in range(return_start_pl,len(s1)):
                if s1[j] == '{':
                    return_start_pl=j
                    break
            return_start_place=len(s)-len(s1[:return_start_pl])-1
            # for j in range(0,return_start_place):
            #     if bb[return_start_place-j] == '{':
            #         return_start_place=return_start_place-j
            #         print(bb[return_start_place-4:return_start_place+4])
            #         print(count)
            #         count+=1
            #         break
            # return_start_place = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}\s*{\s*return',bb).start()
            # return 语句开始部分
            return_end_pl=bb.find('return',return_start_place)
            num=1
            for i in range(return_end_pl+5,len(bb)):
                if bb[i]=='{':
                    num+=1
                elif bb[i]=='}':
                    num-=1
                    if num==-1:
                        return_end_place=i
                        break
            # return_end_place = r.search('{\s*return\s*}', bb).end()
            # return语句结束部分
            dict['return'] = bb[return_start_place:return_end_place]
            # 将return语句写入字典
            flag = 1  # 无限循环标志

            temp = ' '  # 临时字符串
            bb_start_place_flag = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}', bb)
            # print(bb_start_place_flag)
            # if(bb_start_place_flag != None):
            #     print("yes")
            #
            # else:
            #     print("no")
            bb = bb[:return_start_place]
            # print(bb)
            if (bb_start_place_flag != None):

                while (flag):
                    bb_start_place_flag = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}', bb)
                    # 预先搜索bb label 开始部分
                    bb_stop_place_flag = r.search( '{\s*jump\s*{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d*\s*}\s*}\s*leaving\s*\d*\s*}',
                        bb)
                    # 预先搜索bb label 结束部分
                    default_end_place_flag = r.search('{\s*default\s*{\s*label\s*64\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}\s*}\s*}',bb)
                    # 预先搜索bb 中 default 结束部分
                    if (bb_stop_place_flag == None and default_end_place_flag == None):
                        # print("1"+bb)
                        # print("1")
                        if (bb.find('label')==-1):
                            break
                        else:
                            bb_start_place =bb.find('label')
                            bb_st_place=0
                            for i in range(0,bb_start_place):
                                if bb[bb_start_place-i]=='{':
                                    bb_st_place=bb_start_place-i
                                    break

                            for i in range(0,len(bb)):
                                if bb[i]=='}':
                                    bb_en_place=i
                            temp = bb[bb_st_place:bb_en_place+1]
                            dict[r.search('bb\d*', temp).group()] = temp
                            break
                    # 如果再也搜不到则退出循环
                    if (bb_start_place_flag != None):
                        bb_start_place = r.search(
                            '{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}',
                            bb).start()
                    if (bb_stop_place_flag != None):
                        bb_stop_place = r.search(
                            '{\s*jump\s*{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d*\s*}\s*}\s*leaving\s*\d*\s*}',bb).end()
                    if (default_end_place_flag != None):
                        default_end_place = r.search(
                            '{\s*default\s*{\s*label\s*64\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}\s*}\s*}',bb).end()
                    # 判断是否搜得到，搜得到返回索引
                    # 判断是jump语句先出现还是default语句先出现
                    if (default_end_place_flag!=None and default_end_place < bb_stop_place):
                        # print("2")
                        temp = bb[bb_start_place:default_end_place]
                        dict[(r.search('bb\d*', temp)).group()] = temp
                        start=default_end_place
                        end=return_start_place
                        bb = bb[start:end]
                        #start #切片开始位置索引
                        #end #切片结束位置索引
                        # bb语句缩短，从搜到的位置重新开始
                        continue


                    else:
                        # print("3")
                        temp = bb[bb_start_place:bb_stop_place]
                        # print(temp)
                        dict[r.search('bb\d*', temp).group()] = temp
                        start=bb_stop_place
                        end=return_start_place
                        bb = bb[start:end]
                        continue
        # for value in dict.values():
        #     string=value
        #     label_l='"'
        #     start_place=string.find(label_l)
        #     end_place=string.find(label_l,start_place+1)
        #     label=string[start_place+1:end_place]
        #     b_start_place = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}',string).end()
        #     # stringl=string[b_start_place:]
        #     b_start_place = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}',string[b_start_place:]).start()
        #     count=0
        #     while b_start_place!=-1:
        #         start_place=string.find(label,end_place+1)
        #         if string[start_place+len(label)]==':':
        #             bb_old=string[0:b_start_place]
        #             dict[(r.search('bb\d*'+':'+count, bb_old)).group()] = bb_old
        #             count+=1
        #             string=string[b_start_place:]
        #             b_start_place = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}',string).end()
        #             b_start_place = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}',string[b_start_place:]).start()
        #         else:
        #             string=string[b_start_place:]
        #             b_start_place = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}',string).end()
        #             b_start_place = r.search('{\s*label\s*\d*\s*{\s*lref\s*\d*\s*"\w*::bb\d*"\s*}\s*{\s*dec_unsigned\s*\d*\s*\d\s*}\s*}',string[b_start_place:]).start()
        new_dict={}
        # print(dict)
        # dict={'bb':string}
        for key in dict:
            # print(dict[key])
            string=dict[key]
            count=0
            # temp_cout=0
            #print(key)
            even_place=0
            label_l='"'
            start_place=string.find(label_l)
            end_place=string.find(label_l,start_place+1)
            label=string[start_place+1:end_place]
            end_place=0
            start_place=string.find(label)
            # print(label)
            start_place=string.find(label,start_place+len(label))
            while start_place!=-1:
                if string[start_place+len(label)]==':':
                    # print(temp_cout)
                    # temp_cout+=1
                    number=0
                    for i in range(0,start_place):
                        if string[start_place-i]=='{':
                            number+=1
                            if number==2:
                                end_place=start_place-i
                                break

                    if count==0:
                        new_dict[key] = string[even_place:end_place - 1]
                    else:
                        filename_place=string.find('::',even_place)
                        filename_placel = string.find('::',filename_place+1)
                        filename_place_end = string.find('"', filename_placel + 1)
                        filename_sec="_"
                        while(string[filename_placel+2:filename_place_end].find(':')!=-1):
                            filename_sec=filename_sec+string[filename_placel+2:string[filename_placel+2:filename_place_end].find(':')]
                            filename_sec=filename_sec+"_"
                            filename_placel=string[filename_placel+2:filename_place_end].find(':')
                        filename_sec =filename_sec+string[filename_placel+2:filename_place_end]
                        new_dict[key+filename_sec] = string[even_place:end_place-1]
                    # new_dict[key+'_'+str(count)] = string[even_place:end_place-1]
                    # print(even_place)
                    # print(end_place-1)
                    count+=1
                    # print(string[even_place:end_place-1])
                    even_place=end_place
                    # pint('\n')
                    start_place=string.find(label,start_place+len(label))
                else:
                    start_place=string.find(label,start_place+len(label))
            if count!=0:
                filename_place=string.find('::',even_place)
                filename_placel = string.find('::',filename_place+1)
                filename_place_end = string.find('"', filename_placel + 1)
                filename_sec = "_"
                while (string[filename_placel + 2:filename_place_end].find(':') != -1):
                    filename_sec = filename_sec + string[filename_placel + 2:string[
                                                                             filename_placel + 2:filename_place_end].find(
                        ':')]
                    filename_sec = filename_sec + "_"
                    filename_placel = string[filename_placel + 2:filename_place_end].find(':')
                filename_sec =filename_sec+string[filename_placel+2:filename_place_end]
                new_dict[key+filename_sec] = string[end_place:]
            else:
                new_dict[key] = string[end_place:]
            # print (string[end_place:])

            # while start_place!=-1:
            #     #print(start_place)
            #     for s in range(start_place,len(string)):
            #         if string[s]=="}":
            #             end_flag_place=s
            #             break
            #
            #     flag_place=string[start_place:end_flag_place].find(label)
            #     if (flag_place!=-1):
            #         #print(flag_place)
            #         # if(string[flag_place+10:flag_place].find("call")==-1):
            #         if string[flag_place+len(label)]==':':
            #             #print(string[flag_place+len(label)])
            #             for i in range(0,start_place):
            #                 if string[start_place-i]=='{':
            #                     end_place=start_place-i
            #
            #                     break
            #             new_dict[key+'_'+str(count)] = string[even_place:end_place-1]
            #             count+=1
            #             # print(string[even_place:end_place-1])
            #             even_place=end_place
            #             # pint('\n')
            #             start_place=string.find('label',start_place+len('label'))
            #         else:
            #             start_place=string.find('label',start_place+len('label'))
            #     else:
            #         start_place=string.find('label',start_place+len('label'))
            #
            #
                # else:
                #     print("___________________________________________")
                #     start_place=string.find('label',start_place+len('label'))

            # if count!=0:
            #     new_dict[key+'_'+str(count)] = string[end_place:]
            # else:
            #     new_dict[key] = string[end_place:]
            #     #print(start_place)
            #     flag_place_start=string.find(label_l,start_place)
            #     flag_place_end=string.find(label_l,flag_place_start+1)
            #     flag_label=string[flag_place_start+1:flag_place_end]
            #
            #     if flag_label==label:
            #         #print(flag_place)
            #         if string[flag_place_start+len(label)]==':':
            #             #print(string[flag_place+len(label)])
            #             for i in range(0,start_place):
            #                 if string[start_place-i]=='{':
            #                     end_place=start_place-i
            #
            #                     break
            #             new_dict[key+'_'+str(count)] = string[even_place:end_place-1]
            #             count+=1
            #             # print(string[even_place:end_place-1])
            #             even_place=end_place
            #             # print('\n')
            #             start_place=string.find('label',start_place+len('label'))
            #         else:
            #             start_place=string.find('label',start_place+len('label'))
            #     elif flag_label!=label:
            #         start_place=string.find('label',flag_place_end+len('label'))
            # if count!=0:
            #     new_dict[key+'_'+str(count)] = string[end_place:]
            # else:
            #     new_dict[key] = string[end_place:]
            # # print (string[end_place:])
        # file = open('example.alf','w')
        # for ebb in dict:
        #     file.writelines(ebb+'\n')
        #     file.writelines(dict[ebb]+'\n')
        # file.close()
        return new_dict
# print (getBasicBlockSlice(li))
#for bb in list:
#    print(bb+'\n')
# lis=li[0]
# print (getBasicBlockSlice(lis))
# for i in range(0,len(li)):
#         lis=[]
#         lis.append(li[i])
#         print(getBasicBlockSlice(lis))



# for key,value in getBasicBlockSlice(li).items():
#     print('{key}:{value}'.format(key = key, value = value))
