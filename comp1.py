from datetime import datetime
import sys
import argparse

# add positional arguments

parser = argparse.ArgumentParser(description="Log changes of configuration fles ")
parser.add_argument("deployedFile",help='complete path of a deployed file')
parser.add_argument("archivedFile",help='complete path of a archived file')
args = parser.parse_args()


print ("First Argument",args.deployedFile)
print ("Second Argument",args.archivedFile)




#with open('./local.properties') as f:
with open(args.deployedFile) as f:
    t1 = f.read().splitlines()
    t1s = set(t1)

#with open('./local_a.properties') as f:
with open(args.archivedFile) as f:
    t2 = f.read().splitlines()
    t2s = set(t2)

#-- in file1 but not file2
for diff in t1s-t2s:
    print (str(datetime.now()),"Only in file1",t1.index(diff), diff)

#-- in file2 but not file1
for diff in t2s-t1s:
    print (str(datetime.now()),"Only in file2",t2.index(diff), diff)

#send out notification when discrepancy exists
