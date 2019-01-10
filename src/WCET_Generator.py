import os

def WCET_Output(WCETList,FileNameImported):
	File=open(FileNameImported+'.wct','w')
	for key in WCETList:
		File.write(str(key)+' '+str(WCETList[key])+'\n')
	File.close()
