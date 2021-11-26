import os
import shutil
dir1 = os.path.join('1.automating_renaming_files_names','files_to_rename')
dir2 = os.path.join('1.automating_renaming_files_names','renamed_files')
def copy_folder_to_rename_files(src = dir1, dest=dir2):
    '''function copy all files to new folder to see what names of file are at the begining'''
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

def renaming_files(direction=dir2):
    '''function rename all files in ascending order by numbers'''
    os.chdir(direction)
    for f in os.listdir():
        f_name, f_extension = os.path.splitext(f)
        f_planet, f_title, f_number = f_name.strip().split(' - ')
        new_name='{} - {}{}'.format(f_number[1:].zfill(2), f_planet, f_extension)
        os.rename(f,new_name)
copy_folder_to_rename_files()
renaming_files()
