from turtle import position
import os
from bs4 import BeautifulSoup as bs
import vars
from time import strftime, localtime

counter = 0
docFiles = 0
folder = vars.input
txtText = ""

for myfile in os.listdir(folder):

   if myfile.endswith(".doc"):
        file = os.path.join(folder, myfile)
        docFiles += 1
        try:
            soup = bs(open(folder+"\\"+myfile, encoding="ISO-8859-1").read())
            
            [s.extract() for s in soup(['style', 'script'])]
            tmpText = soup.get_text()
            text = "".join("".join(tmpText.split('\t')).split('\n')).strip()
            txtText += text +"\n"
            if "O R P -" in text:    
                txtText += file +"\n"
                position = text.find("O R P -") 
                name = text[position:position+44]
                name = name.replace("-", "_" ).replace("/", "_" ).replace(" ", "" ) 
                name = name + " no" +str(counter) +".doc"
                print(name)
                txtText += name +"\n"
                old_file = os.path.join(folder, myfile)
                new_file = os.path.join(folder, name)
                os.rename(old_file, new_file)
                counter+=1            
        except:  
            pass
print('added name to '+ str(counter) +'/' + str(docFiles) + " doc")
txtText += '\nadded name to '+ str(counter) +'/' + str(docFiles) + " doc"
with open(vars.txt+"\\"+strftime("%Y_%m_%d %H_%M_%S", localtime())+" "+os.path.basename(__file__)+'.txt', 'w', encoding='utf-8') as f:
    f.write(txtText)


        
       


        

 
