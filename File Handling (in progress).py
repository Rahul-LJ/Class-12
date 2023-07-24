#file handling
'''
   2 types of file
     ___________
    |           |
text file    binary file

text file: -Stores data in ascii characters.
           -have EOL (end of line) terminating character '/n'
           -slower in excecution
           -.txt .dat

Binary file: -Stores data in binary characters.
             -No delimiter for a new line
             -faster in excecution
             -.bin .jpeg .exe
_______________________________________________________________________

FILE OPERATION --> open file -> read file -> write file -> close file

open('<filename>') - basically opens the given file name
                     (default opens in read mode)
<filename>.close() - breaks the connection between fileobject and file
________________________________________________________________________

           3 modes              file_object = open('<filename>','mode')
  ________________________
 |      |      |          |
read  write  append  read & write

read only (r) is used to read from existing txt file
write only (w) is used to Create a file by adding string (if file alr exist, it OVERWRITES)
append only (a) same as write to add data but if file alr exist, it creates a new file
read and write (r+) when you want to read aswell as write
________________________________________________________________________


<file_object>.read(n)     - reads the entire file (reads till n bytes)
<file_object>.readline()  - reads 1 word, i.e. reads till a space appears (reads the n)
<file_object>.readlines() - 
'''
