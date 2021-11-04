####    GENERATORS:
def gen(nums):
    for i in range(nums):
        yield i*i
for i in gen(20):
    pass    #print(i)



####    NAMEDTUPLE:
from collections import namedtuple
color = namedtuple("Color",'r g b')
c1=color(55,155,255)
#print(c1[0])
#print(c1.r)


####    CONTEXT MANAGER:
class OpenSample:
    def __init__(self, filename, mode):
        self.filename=filename
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with OpenSample('sample.txt', 'w') as f:
    pass#f.write('Testing')

####    CONTEXT MANAGER with DECORATOR:
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f=open(file,mode)
    yield f
    f.close()

with open_file('sample.txt','w') as f:
    f.write('Testing2')

####    CONTEXT MANAGER OS EXAMPLE:
#without contet manager
import os
cwd = os.getcwd()
os.chdir("1stAnotherCATALOGe")
os.chdir(cwd)

import os
cwd = os.getcwd()
os.chdir("2ndAnotherCATALOGe")
os.chdir(cwd)

#with contet manager
import os
from contextlib import contextmanager

