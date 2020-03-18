import os


list_of_files = os.listdir('/Users/sp/Desktop/Basic-Python-Projects/OS_Module')

for file in list_of_files:
    name, ext = os.path.splitext(file)
    if ext == '.txt':
        file_path = os.path.join('/Users/sp/Desktop/Basic-Python-Projects/OS_Module', file)
        print('The file name is {} and its corresponding modified time is {}.\n'.format(
            file_path, os.path.getmtime(file_path)))

           
