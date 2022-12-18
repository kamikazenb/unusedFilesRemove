from turtle import position
import docx2txt
import os
from random import randrange
import vars
from time import strftime, localtime

counter = 0
docFiles = 0
folder = vars.input 
txtText = "" 
for myfile in os.listdir(folder):
    if myfile.endswith(".docx"):
        docFiles += 1   
        try:
            print(os.path.join(folder, myfile))
            text = docx2txt.process(os.path.join(folder, myfile))
            if "ORP-" in text:
                position = text.find("ORP-") 
                name = text[position:position+21]
                name = name.replace("-", "_" )
                name = name.replace("/", "_" ) 
                name = name + " no" +str(counter) +".docx"
                print(name)
                txtText += name+"\n"
                old_file = os.path.join(folder, myfile)
                new_file = os.path.join(folder, name)
                os.rename(old_file, new_file)
                counter+=1            
        except:
            pass
print('added name to '+ str(counter) +'/' + str(docFiles) + " docx")
txtText += '\nadded name to '+ str(counter) +'/' + str(docFiles) + " docx"
with open(vars.txt+"\\"+strftime("%Y_%m_%d %H_%M_%S", localtime())+" "+os.path.basename(__file__)+'.txt', 'w', encoding='utf-8') as f:
    f.write(txtText)
        
       


        

 
