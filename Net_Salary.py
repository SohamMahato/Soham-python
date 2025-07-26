name=input("enter your name : ")
bs=int(input("enter your basic salary : "))
da=bs*10/100
hra=bs*20/100
ta=bs*5/100
pf=bs*12/100
gs=da+hra+ta
ns=gs-pf
print(name,"net salary is :",ns)
