#hsf
#
#





#jalka nh
sugu = input("sisesta oma sugu: ")
if sugu=="naine":
    print("mine ara")
else:
    print("tsau")
    vanus =int(input("sisesta vanus: "))
if vanus>=16 and vanus<=18:
    print("vastu võetud")
else:
    print("eilol")




#müük
hind = int(input("toote hind krt: "))
if hind<10:
    print("soodustus10%")
if hind>10:
    print("soodukas 20% yo")


#juubel
sp = "5.6.2000"
d,m,y =sp.split(".")
vanus = 2022 - int(y)
print(vanus)
if vanus%5 == 0:
    print("juubel")

else:
    print("ei")



#matemaaika
a,b = 10,20
tehe = input("vali tehe (+ - * /): ")
if tehe =="+":
    vastus = a + b
elif tehe =="-":
    vastus = a - b
    
else:
    vastus = "n/a"
print(f"{a} {tehe} {b} = {vastus}")

#ruut
a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} teevad kokku ristküliku")