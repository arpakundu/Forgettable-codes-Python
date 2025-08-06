####file handling#####
f = open('example.txt') #open file in the current directory
f.colse()

#####cleaner and safer way to save files
try:
    f = open("example.txt")
finally:
    f.close()

#############
f = open("text.txt","r")
f.read(4) ####read first 4 character
f.seek(9) #change to any position for example 9
f.tell(0) #return to current position for example 0

f.seek(0)
for line in f:
    print(line)  ###print line by line
    
f.readline() ##prints upto \n for each line
f.readlines() ## prints the rest of the line of the file
 
#### rename file
import oos
os.rename("text_txt","sample_txt")

####remove/delete file
os.remove("sample_txt")

### find current working directory
os.getcwd()

###changing directory
os.chdir("C:/Users")

#####Find all sub-directories and files
os.listdir(os.getcwd())

###making new directory
os.mkdir('test')

###remove empty directory
os.rmdir('test')

### remove non empty directory
import shutil
shutil.rmtree('non_empty_directory')
