f=open("C://Users//Lava Kumar//Desktop//web programs//reference//python//PythonPrograms//Infosyspythonprogram//FileHandling//rhyme.txt","r");
dict_words={}
list_words=[];
i=0;
for line in f:
    tokens=line.strip().split(" ")
    for token in tokens:
        if(token.lower() not in list_words):
            dict_words[i] = token.lower();
            list_words.insert(i,token.lower());
            i=i+1
    print(tokens)

print(dict_words)
