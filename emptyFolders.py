import os
from posixpath import relpath
from queue import Empty 
import vars
import glob
from pathlib import Path
from time import strftime, localtime

inFolder = vars.input
outFolder = vars.output 
txtText = ""
emptyFolders = 0


for x in range(6):
    folders = 0
    passFirst = 0
    for filename in glob.iglob(inFolder + '**/**', recursive=True):
        onlyFile = os.path.basename(filename)
        relPath = os.path.relpath(filename, inFolder)
        relDirName = os.path.dirname(relPath)
        if passFirst == 0:
            passFirst += 1 
            continue
        
        folders += 1
        if os.path.isdir(filename):
            with os.scandir(filename) as it:
                if any(it):                
                    pass
                else:
                    print(filename)
                    txtText += f'{filename}\n'     
                    emptyFolders += 1
                    old_file = os.path.join(filename)
                    new_file = os.path.join(outFolder, onlyFile)
                    if os.path.dirname(relPath):
                        Path(os.path.join(outFolder, relDirName)).mkdir(parents=True, exist_ok=True) 
                        new_file = os.path.join(outFolder, relPath)
                        try:                            
                            os.rename(old_file, new_file)
                            continue 
                        except:                            
                            txtText += f'ERROR move {filename}\n' 
                            print("ERROR move "+filename)
                            pass
                        try:
                            os.rmdir(old_file)                             
                            continue 
                        except:
                            print("ERROR delete "+filename)
                            txtText += f'ERROR delete {filename}\n'  
                            pass     

    print(f'iteration {x} \nfolders {folders} \nempty folders {emptyFolders} \n' )
    txtText += f'\niteration {x} \nfolders {folders} \nempty folders {emptyFolders} \n'   

print(f'total empty folders {emptyFolders}')
txtText += f'total empty folders {emptyFolders}'
with open(vars.txt+strftime("%Y_%m_%d %H_%M_%S", localtime())+" "+os.path.basename(__file__)+'.txt', 'w', encoding='utf-8') as f:
    f.write(txtText)