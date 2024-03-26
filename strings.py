def plus(s:str,cc:int):
    count:int=cc
    c=s.split('+')
    clen=len(c)
    v:str="var"+str(count)
    for n in range(clen):
        
        v:str="var"+str(count)
        if n==0:
            print(v + '=addstring('+c[0]+','+c[1]+')'  )
            
        elif n==1:
            pass
        else:
            print(v+'=addstring('+v+','+c[n]+')')

        

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
                v:str="var"+str(count)
                print(v+'="'+c[n]+'"')
                vv='"'+c[n]+'"'
                s=s.replace(vv,v)
                count+=1
    print(s)
    plus(s,count)
    

pre='"hello"+"world"+"hi"+"...."'
print("\x1bc\x1b[44;37mprecompiler.....")
preprocessor(pre)