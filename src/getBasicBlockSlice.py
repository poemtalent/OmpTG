# getBasicBlockSlice
import os
import re as r #正则表达式库
import sys
def getBasicBlockSlice(list):
        for bb in list:
            bb_dict = {}  # 创建字典
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
            bb_dict['return'] = bb[return_start_place:return_end_place]
            # print(bb[return_start_place:return_end_place])
            # 将return语句写入字典
            # findPosFromPoint

            bb_body=bb[:return_start_place]

            start_bb_place=0
            end_bb_place = 0
            start_bb_flag=bb_body.find("label")
            while start_bb_flag!=-1:
                bb_temp = ''
                bb_temp=findPosFromPoint(bb_body,start_bb_place)
                start_bb_place = bb_body.find(bb_temp, start_bb_place)
                end_bb_place=bb_body.find(bb_temp,start_bb_place)+len(bb_temp)
                bb_temp = findPosFromPoint(bb_body, end_bb_place)
                end_bb_place = bb_body.find(bb_temp,end_bb_place)+len(bb_temp)
                bb_temp=bb_body[start_bb_place:end_bb_place+1]
                start_bb_place=end_bb_place
                bb_name=(r.search('bb\d*', bb_temp)).group()
                start_bbname_place=bb_temp.find(bb_name)
                end_bbname_place=bb_temp.find('"',start_bbname_place)
                bb_namebody=bb_temp[start_bbname_place:end_bbname_place]
                bb_realname=''
                st=0
                while bb_namebody.find(":",st)!=-1:
                    for i in range(bb_namebody.find(":",st), len(bb_namebody)):
                        if bb_namebody[i]!=":":
                            bb_realname = bb_realname+bb_namebody[st:bb_namebody.find(":",st)] +'_'
                            st=i
                            break
                bb_realname=bb_realname+bb_namebody[st:]
                bb_dict[bb_realname]=bb_temp
                start_bb_flag = bb_body.find("label",start_bb_place)
                # dict[(r.search('bb\d*', temp)).group()] = temp
        return bb_dict

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