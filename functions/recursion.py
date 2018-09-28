def multiple(num):
    if(num==0):
        return False;
    else:
        print("3*",num," = ",3*num)
        return  multiple((num-1))

multiple(10)