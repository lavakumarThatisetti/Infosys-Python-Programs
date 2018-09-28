f=open("C://Users//Lava Kumar//Desktop//web programs//reference//python//PythonPrograms//Infosyspythonprogram//FileHandling//stu_records.txt","r");
dict_records={};
list_records=[];
i=0;
for line in f:
    list_records.insert(i,line.strip());
    dict_records[i]=line.strip();
    i=i+1
print(list_records)
print(dict_records)