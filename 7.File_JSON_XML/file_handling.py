'''f=open('input.txt',"w+")
print(f.tell())     #give possition of pointer
f.write('I\'m devoite of Radhe')
print(f.tell())
f.seek(4,0)
print(f.tell())
content=f.read()
print(f.tell())
print(content)'''

#seek(offset,postion)
# offset->number of char
# position->0->stat of the file
#           1->current position
#           2->end of the file
# seek(15,0)-> change the f by 15 char from start of the file
# seek(0,2)-> change the f by 0 char from end of the file
# seek(15,1) and seek(15,2)->not allowed

# r+ = read + write (don't remove old content)

'''f1=open('input.txt','r+')
content=f1.read()
print(content)

f1.write('. Hari bol!!')'''

# append a & a+ -> file pointer at end
# r,r+ -> when file open file pointer position is at start
# w,w+ ->  when file open file pointer position is at start

f2=open('input.txt','a+')   # a -> allow only write operation
'''f2.write('Radhe Radhe..')'''

print(f2.tell())
content=f2.read()
print(content)

'''
r  -> file_pointer -> start , file should already exits , read
r+ -> file_pointer -> start , file should already exits , read and write

w -> file_pointer -> start , file should already exits, write
w+ -> file_pointer -> start , file should already exits, write + read

a -> file_pointer -> end ,create new file , write at the end
a+ -> file_pointer -> .end , create new file,read + write

'''