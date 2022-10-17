#Tõnis Kändmaa
#17.10.2022
#harjutus3

#palimdroom

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "racecar"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")






#tundide jad
a1,a2 = "8:30", "14:15"
h1,m1 = a1.split(":")
minut1 =int(h1)*60+int(m1)
h2,m2 = a2.split(":")
minut2 =int(h2)*60+int(m2)
ajavahe =minut2-minut1


hh = ajavahe//60
mm = ajavahe%60
print(f"ajavahe on {hh}:{mm}")


#email
email = "sdsaffs@fssf.sds"
print("@" in email)



#vandumine
tekst = input("ütle kurat küll!:")
print(tekst.lower().replace("kurat","***"))
