def preprocessor(s:str):
    count:int=0
    c=s.split('"')
    clen:int=len(c)
    cclen=clen & 1
    if clen==1:
        print("dont have string")
    else:
        if cclen==0:
            print("string is not close")
        else:
            for n in range(1,clen,2):
                print("var"+str(count)+'="'+c[n]+'"')
                count+=1

pre='"hello"+"world"+"hi"+"...."'
print("\x1bc\x1b[44;37mprecompiler.....")
preprocessor(pre)