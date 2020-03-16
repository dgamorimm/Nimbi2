import os
import shutil
sourcepath='C:/Nimbi/Requisição/'
os.mkdir(sourcepath + "88888")
sourcefiles = os.listdir(sourcepath)
destinationpath = 'C:/Nimbi/Requisição/88888'
for file in sourcefiles:
    if file.endswith('.zip'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))