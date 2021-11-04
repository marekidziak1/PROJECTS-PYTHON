
import os
#non absolute path
#hello_txt=os.path.join('templates','hello_world.txt')
this_file_path=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(this_file_path)
hello_txt=os.path.join(BASE_DIR,'templates','hello_world.txt')

print(hello_txt)
content=""
with open(hello_txt,'r') as f:
    content=f.read()
print(content)
