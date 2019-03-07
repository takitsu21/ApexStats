import os

path = os.path.dirname(os.path.abspath(__file__))
os.system('PowerShell')
os.system('cd {}'.format(path))
print(os.system('PowerShell ls'))
