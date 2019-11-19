#https://github.com/laragon-byte/CSCI-week12-utility
#Leonardo Aragon
#CSCI 102-Section C
#Week 11-Part B

def PrintOutput(string):
    print('OUTPUT',string)

def LoadFile(file):
    read_file=open(file,"r")
    unedited=read_file.read()
    read_file.close()
    l = []
    for line in in_file:
        l.append(line.split(','))
    print('OUTPUT', l)


    
