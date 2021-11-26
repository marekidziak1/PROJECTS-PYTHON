fname='hello_world.txt'
#writing
file_object=open(fname, 'w')
file_object.write("Hello World")
file_object.close()
#reading
file_object=open(fname, 'r')
text=file_object.read()
print(text)
file_object.close()
#writing and reading in 'with option'
with open(fname, 'w') as file_object:
    file_object.write('hi guys')
with open(fname, 'r') as file_object:
    text=file_object.read()
    print(text)