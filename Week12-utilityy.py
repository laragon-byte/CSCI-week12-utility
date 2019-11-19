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

def ScoreFinder(players, scores, name):
    check=0
    counter=-1
    index=0
    listt=[]
    name_lower=name.lower()
    print(name)
    for i in players:
        i=i.lower()
        listt.append(i)
    for i in listt:
        counter+=1
        if i==name_lower:
            check+=1
            index=counter
    if check==0:
        print('OUTPUT player not found')
    else:
        score=scores[index]
        print('OUTPUT', name,'got a score of', score)
def Union(list1,list2):
    for i in list2:
        list1.append(i)
    print('OUTPUT', list1)

def Intersection(list1,list2):
    output=[]
    for i in list1:
        for j in list2:
            if i==j:
                output.append(i)
    print('OUTPUT', output)


        


    
