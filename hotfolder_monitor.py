import yaml
from datetime import datetime

#0. read configuration

with open("./hotfolder.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
#. load file prefix of IP

for section in cfg:
    print(section)
print(cfg['ip13']['file_prefix'])
prefix_list = cfg['ip13']['file_prefix']
log_file = cfg['ip13']['log_file']


#/home/jerry/dev/tmp#


from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('/home/jerry/dev/tmp') if isfile(join('/home/jerry/dev/tmp', f))]

print(onlyfiles)


def find_runid():
    for prefix in prefix_list:
        for filename in onlyfiles:
            if prefix in filename:
                return '41003'
            else:
                print("NOT Found")


def check_done_status(runid):
    if len(onlyfiles) == 0:
        return True
    for filename in onlyfiles:
        if runid in filename:
            return False


def log_files_left(runid, log_location= log_file):
    for filename in onlyfiles:
        if runid in filename:
            locallog('---  '+filename,history_file=log_location)


def locallog(message, rw_flag='a+',history_file=log_file):
    history = open(history_file, rw_flag)
    history.write(str(datetime.now())+message)
    history.write("\n")

# find run id
print(find_runid())

# progress status
if check_done_status(find_runid()) == True:
    locallog(' IP13 completely consumed', rw_flag='w')
else:
    # log left files
    locallog(' Left files:',rw_flag='w')
    log_files_left(find_runid())



#. monitor the change of file number
#. report left files