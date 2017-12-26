from datetime import datetime
import sys
import argparse
import os
import shutil


def locallog(message,historyFile='history.txt'):
    history = open(historyFile,"a+")
    history.write(message)
    history.write("\n")

def compareConfigFiles(deployedFile,archivedFile):

    with open(deployedFile) as f:
        t1 = f.read().splitlines()
        t1s = set(t1)



    with open(archivedFile) as f:
        t2 = f.read().splitlines()
        t2s = set(t2)

    #-- in file1 but not file2
    for diff in t1s-t2s:
        log1="%s Only in deployed file %s %s \n"%(str(datetime.now()),t1.index(diff), diff)
        print (log1)
        locallog(log1)
        #history.write(log1)
        #history.write("\r\n")
        #print (str(datetime.now()),"Only in file1",t1.index(diff), diff)

    #-- in file2 but not file1
    for diff in t2s-t1s:
        log2="%s Only in archived file %s %s \n"%(str(datetime.now()),t2.index(diff), diff)
        print (log2)
        locallog(log2)
        #history.write(log2)
        #history.write("\r\n")


#-- add positional arguments

parser = argparse.ArgumentParser(description="Log changes of configuration fles ")
parser.add_argument("deployedFile",help='complete path of a deployed file')
parser.add_argument("archivedFile",help='complete path of a archived file')
args = parser.parse_args()


print ("First Argument",args.deployedFile)
print ("Second Argument",args.archivedFile)




if not os.path.isfile(args.deployedFile):
    print("stop compare and add logs")
    msg="%s Deplyed file not exists \n"%(str(datetime.now()))
    locallog(msg)
else:
    print("deployed file exists")
    if os.path.isfile(args.archivedFile):
        print("archived file exists")
        compareConfigFiles(args.deployedFile,args.archivedFile)
    else:
        print("archived file not exits")
        shutil.copy2(args.deployedFile,args.archivedFile)
        msg="%s Archived file not exists; Copied deployed file \n"%(str(datetime.now()))
        locallog(msg)







#send out notification when discrepancy exists
