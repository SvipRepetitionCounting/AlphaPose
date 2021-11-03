import os

from video2json import video2json
from pull_up import pullup_count
from situp import situp_count
from jump_rope import JumpCount
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filePath', help='file path')
parser.add_argument('sportType', help='sport type')
args = vars(parser.parse_args())
filepath = args['filePath']
type = args['sportType']

if not os.path.exists(filepath):
    print('please input right file path')
else:
    data_dir,filename = os.path.split(filepath)
    jsonpath = video2json(data_dir,filename)

    if "jumprope" in type.lower():
        jump = JumpCount(jsonpath)
        count = jump.run()
    elif "situp" in type.lower():
        count = situp_count(jsonpath)
    elif "pullup" in type.lower():
        count = pullup_count(jsonpath)
    else:
        print('type error')
#     print(count)