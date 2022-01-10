#Írj ki egy stringet txt fájlba!

kiirando_szoveg="Erik, ne püföld annyira a billentyűzetet!"

celfajl=open("erik.txt","w")

print(kiirando_szoveg,file=celfajl)

celfajl.close()
