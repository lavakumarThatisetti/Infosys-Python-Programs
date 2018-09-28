f2=open("C://Users//Lava Kumar//Desktop//web programs//reference//python//PythonPrograms//Infosyspythonprogram//FileHandling//testfile2.txt","w+");
with open("C://Users//Lava Kumar//Desktop//web programs//reference//python//PythonPrograms//Infosyspythonprogram//FileHandling//testfile1.txt",'r') as f1:
    while True:
        c=f1.read(1)
        if(c=='"'):
            f2.write("\\")
        if not c:
            break;
        f2.write(c)
        print(c,end=" ")



