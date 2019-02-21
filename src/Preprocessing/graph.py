import networkx as nx
import re
#=========================
from src.Preprocessing.PreprocessDot import preprocess
#=========================

dotPath='dot/task2.dot'
relationPath='dot/relation.txt'
parseFunction='_taskFunc2_'

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
    nodesIter=nx.nodes(graph)

    for callBlock in relationDict.keys():
        #查找图中的callBlock
        pass
    pass


if __name__=='__main__':
    relation = parseRelation(relationPath)
    preprocess(dotPath)
    graph = nx.nx_pydot.read_dot(dotPath+'tmp')#'Preprocessing/knapsack_ompi_trim.Preprocessing')
    parse(parseFunction,graph,relation)










