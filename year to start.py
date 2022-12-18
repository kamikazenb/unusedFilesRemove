from turtle import position
import os
import re
import vars
from time import strftime, localtime

counter = 0
docFiles = 0
folder = vars.input
txtText = ''

for myfile in os.listdir(folder):
    if myfile.endswith((".doc", ".docx")):
        docFiles += 1
        if myfile.startswith("ORP"):
            result = re.search('20[1-2][0-9]', myfile)
            if result:             
                name = result.group() + " " +myfile
                print(name)
                txtText += name + '\n'
                old_file = os.path.join(folder, myfile)
                new_file = os.path.join(folder, name)
                os.rename(old_file, new_file)
                counter += 1
print('renamed '+ str(counter) +'/' + str(docFiles) + " doc|docx")
txtText += '\nrenamed '+ str(counter) +'/' + str(docFiles) + " doc|docx"
with open(vars.txt+"\\"+strftime("%Y_%m_%d %H_%M_%S", localtime())+" "+os.path.basename(__file__)+'.txt', 'w', encoding='utf-8') as f:
    f.write(txtText)

