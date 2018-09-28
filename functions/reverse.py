def reverse(num):
    if(len(num)==0):
        return num;
    else:
        print(num[1:])
        return reverse(num[1:])+num[0];


print(reverse("lava"))

