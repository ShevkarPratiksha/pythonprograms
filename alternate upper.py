try:
    f1=open("sample.txt",'r')
    f2=open("sample.txt4",'w')
    x=f1.read()
    s=len(x)
    for i in range(s):
        if i  % 2== 0 :
            f2.write(x[i].upper())
        else:
            f2.write(x[i].lower())    
    f1.close()
    f2.close ()       
except:
    print("File Error") 