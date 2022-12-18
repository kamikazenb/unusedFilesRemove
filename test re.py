import re

pattern = '20[1-2][0-9]'
test_string = 'a 20915445646546'
result = re.search(pattern, test_string)
if result:            
    print(result.group())

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	