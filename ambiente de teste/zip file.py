import fnmatch
import os

for file in os.listdir('C:/Nimbi/Requisição/'):
    if fnmatch.fnmatch(file, '*.zip'):
        print(file)

os.f