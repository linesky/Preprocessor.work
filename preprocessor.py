def preprocessor(s:str):
    c=s.split(")")
    cc=c[0].split("(")
    clen:int=len(c)
    cclen:int=len(cc)
    if clen!=cclen:
        print("error on parentices")
    else:
        for n in range(clen):
            
            if n==0:
                print(cc[clen-n-1])
            else:
                print(cc[clen-n-1]+"()"+c[n])

pre="sub1(sub2(sub3(sub4(5)+4)+3)+2)+1"
print("\x1bc\x1b[44;37mprecompiler.....")
preprocessor(pre)