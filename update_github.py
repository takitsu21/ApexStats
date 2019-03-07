import os

path = os.path.dirname(os.path.abspath(__file__))
os.system('cd {} && git add . && git commit -m "{}" && git push origin master'.format(path,input('commit : ')))
