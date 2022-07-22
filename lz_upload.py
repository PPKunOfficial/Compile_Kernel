from gettext import find
from re import S
from lanzou.api import LanZouCloud
import sys,re

first=sys.argv[1]
sec=sys.argv[2]


login_cookie={
    "ylogin":first,
    "phpdisk_info":sec
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
