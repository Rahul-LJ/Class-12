#FILE HANDLING
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
  _____________
 |      |      |
read  write  append

read only (r)       is used to read from existing txt file
write only (w)      is used to Create a file by adding string (if file alr exist, it OVERWRITES)
append only (a)     same as write to add data but if file alr exist, it creates a new file
read and write (r+) when you want to first read then write
write and read (w+) when you want to first write (overwrite) then read it
________________________________________________________________________

#remember these func moves the pointer!
<file_object>.read(n)     - reads the entire file if no argument (reads till n bytes)

<file_object>.readline()  - reads till EOL if no argument (reads till n bytes)

<file_object>.readlines() - reads entire file if no argument in a LIST (reads n lines)

<file_object>.write()     - to add data to a file
                            if file alr exists, it'll overwrite (deletes the old, and writes the new)
                            {print of this function gives you the No.Of.Characters in write}
                            {if used in r+ mode, it REPLACES the required No.Of.Chr to the Existing one with the new}
                            
<file_object>.writelines()- to add a LIST of data. To add many values.
                            (eg: l = ['line1','\nline2'] )

<file_object>.seek()      - for 1 argument
                            move the pointer after the given pos.of character (eg: seek(1) comes b/w 1,2 character)

                            for 2 arguments (ONLY FOR BINARY only)
                            <file_object>.seek( no of STEPS to move left (-ve) or right (+ve) , FROM )
                            where FROM can be 0 - beghinning of the file
                                              1 - current position
                                              2 - end of the file

'''
