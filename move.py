import os
from posixpath import relpath
from queue import Empty 
import vars
import glob
from pathlib import Path
from time import strftime, localtime

files = 0
folders = 0
emptyFiles = 0
tmpFiles = 0
emptyFolders = 0
inFolder = vars.input
outFolder = vars.output 
minFileSize = vars.minFileSize
txtText = ""



for filename in glob.iglob(inFolder + '**/**', recursive=True):
    onlyFile = os.path.basename(filename)
    relPath = os.path.relpath(filename, inFolder)
    relDirName = os.path.dirname(relPath)
        
    if os.path.isdir(filename):           
        folders += 1
        continue

    files += 1
    if filename.endswith(".tmp"):
        tmpFiles += 1

    if os.path.getsize(os.path.join(inFolder, filename))  < minFileSize:
        emptyFiles += 1 

    if os.path.getsize(os.path.join(inFolder, filename)) < minFileSize or filename.endswith(".tmp"):
        print(str(os.path.getsize(filename)) + " "+ filename )
        txtText += str(os.path.getsize(filename)) + " "+ filename+'\n'
        old_file = os.path.join(filename)
        new_file = os.path.join(outFolder, onlyFile)
        if os.path.dirname(relPath):
            Path(os.path.join(outFolder, relDirName)).mkdir(parents=True, exist_ok=True) 
            new_file = os.path.join(outFolder, relPath)
        os.rename(old_file, new_file)



print(f'total files {files} \ntotal folder {folders}\n{minFileSize}b files {emptyFiles}\n.tmp files {tmpFiles}' )
txtText += f'\ntotal files {files} \ntotal folder {folders}\n{minFileSize}b files {emptyFiles}\n.tmp files {tmpFiles}'
with open(vars.txt+"\\"+strftime("%Y_%m_%d %H_%M_%S", localtime())+" "+os.path.basename(__file__)+'.txt', 'w', encoding='utf-8') as f:
    f.write(txtText)