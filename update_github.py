import os

path = os.path.dirname(os.path.abspath(__file__))
# os.system('PowerShell')
os.system('cd {} && git add . && git commit -m "{}" && git push origin master && takitsu21 && takipro21'.format(path,input('commit : ')))
# print(os.system('PowerShell ls'))
