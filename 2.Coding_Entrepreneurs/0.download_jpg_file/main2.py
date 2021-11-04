import os
import requests
import shutil
def f():
    BASE_DIR= os.path.dirname(os.path.abspath(__file__))
    files_dir=os.path.join(BASE_DIR,"images")
    os.makedirs(files_dir,exist_ok=True)
    for i in range(1,3):
        fname=f'{i}_2.jpg '
        file_path=os.path.join(files_dir,fname)
        if os.path.exists(file_path):
            print('path exists')
            continue
        url='https://static.wikia.nocookie.net/lotr/images/e/e3/Lonely_Mountain_-_DoS.jpg/revision/latest?cb=20200317224945'
        print(os.path.basename(url))
        with requests.get(url=url,stream=True) as r:
            with open(file_path,'wb') as file:
                shutil.copyfileobj(r.raw, file)
if __name__=='__main__':
    f()