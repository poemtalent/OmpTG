import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import re

#=========================
from src.Preprocessing.PreprocessDot import preprocess
#=========================

#设置工作目录
root='/home/kingtous/Desktop/bots-master/omp-tasks/nqueens/thr/'

#=======DOT存放位置===============
dotPath=root+'nqueens_sweet.dot'
#=======relation.txt存放位置======
relationPath=root+'_thrFunc0_relation.txt'
#=======需要处理的函数入口（暂时不用）======
parseFunction='_thrFunc0_'
#=======dot输出==========
dotOutput=root+'thrFunc0_pro.dot'

def parseRelation(Path):
    '''
    :param Path: path to relation file
    :return: Dict [key:basic block] [value: Function to be called]
    '''
    relationDict={}
    file=open(Path,'r')
    while True:
        line=file.readline().strip()
        if line=='':
            break
        else:
            KeyValue=re.split('\s+',line.replace(':','_'))
            relationDict[KeyValue[0]]=KeyValue[1]
    return relationDict



def parse(parseFunction,graph,relationDict):
    '''
    :param parseFunction: 要处理的函数
    :param graph: networkx处理生成的图数据
    :param relationDict: 关系字典，basicblock:callFunction
    :return: graph 拼接的图文件
    '''
    #获取图中所有节点
    try:
        for callBlock in relationDict.keys():
            #查找图中的callBlock,连接callBlock以及函数entry,exit连接callBlock的下一条边
            if relationDict[callBlock].startswith('ort_'):
                graph.node[callBlock]['label']='('+callBlock.split('__bb')[0]+')'+relationDict[callBlock][4:]
                continue
                #callBlockNode = nx.get_node_attributes(graph, callBlock)
            else:
                graph.node[callBlock]['label'] = 'CALL ' + relationDict[callBlock]
            Function_entry=relationDict[callBlock]+'_entry'
            Function_exit=relationDict[callBlock]+'_exit'
            nextNode=None

            for nod in nx.neighbors(graph,callBlock):
                nextNode=nod
            graph.add_edge(Function_exit,nextNode)
            graph.add_edge(callBlock, Function_entry)
            # 删去不必要的边
            graph.remove_edge(callBlock,nextNode)
    except:
        print('名称与结点名不对应.')
        exit(-1)



if __name__=='__main__':
    relation = parseRelation(relationPath)
    preprocess(dotPath)
    graph = nx.nx_pydot.read_dot(dotPath+'tmp')#'Preprocessing/knapsack_ompi_trim.Preprocessing')
    parse(parseFunction,graph,relation)
    write_dot(graph,dotOutput)
















