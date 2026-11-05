for i in range(2,101):
    premier = True
    for j in range(2,int((i/2)+1)):
        if (i%j) == 0:
            premier = False
    if premier :
        print(i)
