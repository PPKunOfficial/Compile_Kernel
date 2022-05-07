from gettext import find
from re import S
from lanzou.api import LanZouCloud
import sys,re

# login data
def reComArgv():
    first=sys.argv[1]
    sec=sys.argv[2]
    my_re = re.compile(r'[A-Za-z]',re.S)
    res=re.findall(my_re,first)
    if len(res):
        return [sec,first]
    else:
        return [first,sec]

login_cookie={
    "ylogin":reComArgv()[0],
    "phpdisk_info":reComArgv()[1]
}

# login
lzcloud=LanZouCloud()
code=lzcloud.login_by_cookie(login_cookie)
print(code)

# folders
folders=lzcloud.get_move_folders()
find_actions=folders.find_by_name("actions_upload")
if(find_actions==None):
    fid=lzcloud.mkdir(-1,"actions_upload")

# upload 
lzcloud.upload_file(folder_id=fid,file_path=sys.argv[3])

# logout
lzcloud.logout()
