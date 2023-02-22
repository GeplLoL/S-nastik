def loe_failist(f):
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def tõlk(f:str,s:str):
    x=input("Sise sõnu: ")
    if x in f:
        asv=f.index(x)
        asd=s[asv]
    else:
        asd="Vale sõnu"
    return(asd)
def lisa_sõnu(f:str,s:str):
    x=input("Esti sõna: ")
    y=input("Vene sõna: ")
    asv=f.append(x)
    asd=s.append(y)
    return(asv,asd)
def muutaSõnu(f:str,s:str):
    xy=input("millist sõnastikku soovite parandada? Est või Vene")
    if xy=="Est":
        x=input("Nimetage sõna asukoht: ")
        xyz=input("Sisse: ")
        ind=f.index(x)
        f=f.insert(ind,xyz)
       
    elif xy=="Vene":
        y=input("Nimetage sõna asukoht: ")
        xyz=input("Sisse: ")
        ind=f.index(y)
        s=f.insert(ind,xyz)
    return f,s
