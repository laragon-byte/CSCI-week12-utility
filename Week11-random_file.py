#Leonardo Aragon
#CSCI 102-Section C
#Week 11-Part A

def clean_word(string):
    #partially adapted from geeksforgeeks.org
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
   
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "")
    string=string.lower()
    string=string.replace(' ','')

    return string
#print(clean_word('WelCome ?><^$^& to Mora!?'))

def read_file(file):
    read_file=open(file,"r")
    unedited=read_file.read()
    read_file.close()
    unedited=unedited.split()
    listt=[]
    for i in unedited:
        i=clean_word(i)
        listt.append(i)
        #print(i)
    #print(listt)
    return listt

#print(read_file('sample_file.txt'))
    
def write_file(listt,output_file,num_words,seed):
    x=open(output_file,'w')
    counter=0
    output=[]
    import random
    random.seed(seed)
    while counter<int(num_words):
        word=random.choice(listt)
        output.append(word)
        counter+=1
    output=str(output)
    x.write(output)
    x.close()
    return output
#print(write_file(read_file('sample_file.txt'),'week11_output.txt',5,4))
write_file(read_file('sample_file.txt'),'sample_output.txt',20,0)     
#I wasnt sure how the function was going to be called, I hope this works    
    




