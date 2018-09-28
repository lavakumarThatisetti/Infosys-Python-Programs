with open("C://Users//Lava Kumar//Desktop//web programs//Learn//pythontmathtxt.txt") as f:
    print(f.read())
for line in f:
    token=line.split(" ");
    print(len(token))