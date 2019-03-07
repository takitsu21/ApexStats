import os

path = os.path.dirname(os.path.abspath(__file__))
# os.system('PowerShell')
os.system('cd {} && git add . && git commit -m "{}" && git push origin master'.format(path,input('commit : ')))
os.system('takitsu21')
os.system('takipro21')
# print(os.system('PowerShell ls'))
