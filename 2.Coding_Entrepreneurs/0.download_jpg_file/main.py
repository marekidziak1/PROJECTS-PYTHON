import os
import requests
def f():
    BASE_DIR= os.path.dirname(os.path.abspath(__file__))
    files_dir=os.path.join(BASE_DIR,"images")
    os.makedirs(files_dir,exist_ok=True)
    for i in range(1,3):
        fname=f'{i}.jpg '
        file_path=os.path.join(files_dir,fname)
        if os.path.exists(file_path):
            print('path exists')
            continue
        with open(file_path,'wb') as f:
            url='https://static.wikia.nocookie.net/lotr/images/e/e3/Lonely_Mountain_-_DoS.jpg/revision/latest?cb=20200317224945'
            r=requests.get(url=url,stream=True)
            f.write(r.content) 
if __name__=='__main__':
    f()