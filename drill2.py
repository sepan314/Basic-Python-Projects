#Author: Serena Pan
#Date: 3/18/2020
#File: practice using databases and sqlite3

import sqlite3

txt_files = []
db_name = 'drill2.db'

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#extract all files with .txt extension
for file in fileList:
    name, ext = file.split('.')
    if ext == 'txt':
        txt_files.append(file)
        
#creating and querying database
conn = sqlite3.connect(db_name)

with conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tbl_file( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)')
    cursor.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
        (txt_files[0],))
    cursor.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
        (txt_files[1],))
    conn.commit()

conn.close()

conn = sqlite3.connect(db_name)

with conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_file')
    file_name = cursor.fetchall()
    for file in file_name:
        print ("Qualifying files: " + file[1])
    


