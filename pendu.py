import os

def prestationjeu():
    print("******************************************************")
    print("******************* LE PENDU ! ***********************")
    print("******************************************************")
    print("")
    print("")


#effacer la console avec le mot à découvrir
os.system("cls") # pour linus os.system("clear")
prestationjeu()    

mot = input("le mot à découvrir est : ").upper()
mot_decouvert =[]
mot_a_decouvrir=[]
lettres_donnees=""
mot_temp=""
bOK=False

os.system("cls") 
prestationjeu()

for l in mot:
    mot_a_decouvrir.append(l)
    mot_decouvert.append("_")
    
i=0
while i<=7:    
    lettre = str(input("entrer une lettre : "))[0:1].upper()

    os.system("cls") 
    prestationjeu()
    
    lettres_donnees=lettres_donnees + " " + lettre
    print("Lettres proposées :",lettres_donnees)
    print("")
    p=0
    bOK=False
    for l in mot_a_decouvrir: 
       # print(l,str(p))       
        if l==lettre: 
            bOK=True          
            mot_decouvert[p]=l
        p+=1
    #si bonne lettre on garde le nombre d'essai
    if not bOK:
        print("Mauvaise lettre !")
        i+=1    
    else:    
        print("Bonne lettre !")
    mot_temp=''.join(map(str,mot_decouvert))
    print("")
    print(mot_temp)
    print("")
    print("Le mot est-il découvert ?",str(mot==mot_temp))
    print("Nombre d'essais restant :",str(8-i))
    print("")
    if mot==mot_temp:
        break

    

if mot==mot_temp:
    print("C'est gagné !")
else:
    print("C'est perdu!","Le mot est",mot)

sortie=input("Taper une lettre sur le clavier pour fermer !")