f=open("C://Users//Lava Kumar//Desktop//web programs//reference//python//PythonPrograms//Infosyspythonprogram//FileHandling//courses.txt","r");
dict_courses={};
list_Courses=[];
i=0;
for line in f:
    list_Courses.insert(i,line.strip());
    dict_courses[i]=line.strip();
    i=i+1
print(list_Courses)
print(dict_courses)