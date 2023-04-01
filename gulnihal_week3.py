
#soru1
liste= [2,12,9,50,7,66,91,14,143,23,48,19,100,71,28]

a=int(input("Lutfen listeye eklemek istediginiz sayiyi giriniz:"))
liste.insert(0,a)

liste_tek=[]
for i in liste:
    if i%2==1:
        liste_tek.append(i)
        liste.remove(i)
    else:
        pass    
        

liste.sort()
liste_tek.sort()
print(liste)
print(liste_tek)

#soru2
liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]
a=liste[2][1]
print(a)
son=liste[-1]
print(son)
sayilar=[]
sayilar.append(liste[3:7])
print(len(sayilar))

a=[i for i in range(101) if i%10==0]
print(a)

