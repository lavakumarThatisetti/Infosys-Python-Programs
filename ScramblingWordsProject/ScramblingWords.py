import random
textfile=open("C://Users//Lava Kumar//Desktop//web programs//reference//python//PythonPrograms//Infosyspythonprogram//ScramblingWordsProject//textfile.txt","r");
scrambledfile=open("C://Users//Lava Kumar//Desktop//web programs//reference//python//PythonPrograms//Infosyspythonprogram//ScramblingWordsProject//scrambledfile.txt","w+");
for line in textfile:
    tokens=line.strip().split(" ");
    for token in tokens:
        if(len(token)<=3):
            token=token+" ";
            scrambledfile.write(token);
        else:
            token_len=len(token);
            for i in range(1,token_len-1):
                num1 = random.randrange(1, token_len-1);
                num2 = random.randrange(1, token_len-1);
                s = list(token)
                s[num1] = token[num2]
                s[num2] = token[num1];
            new_token="".join(s)+" ";
            scrambledfile.write(new_token);








