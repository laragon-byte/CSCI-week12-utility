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

def UpdateString(string1, string2, index):
    string10=''
    counter=-1
    for i in string1:
        counter+=1
        if counter==index:
            i=string2
        string10+=i
    print('OUTPUT', string10)

def FindWordCount(listt,string):
    counter=0
    for i in listt:
        if i==string:
            counter+=1
    print('OUTPUT',counter)


    
