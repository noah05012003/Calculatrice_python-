from tkinter import *


fenetre = Tk()
fenetre.configure(background="#101419")
fenetre.title("Calculatrice de Noah")
fenetre.geometry("235x385")
fenetre.mainloop()

equation = StringVar() #variable qui va stocker
resulat = Label(fenetre,bg="#101419",fg="#FFF",textvariable = equation, height= "2")
resulat.grid(colomnspan=4)

#BOUTONS
boutons = [7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","="]
ligne = 1
colonne = 0
for button in boutons:
    bt = Label(fenetre,text = str(boutton),bg = "#476C9B",fg= "#FFF",height = 4, width =6)
    bt.bind("<Button-1>", print) #rendre le texte cliquable
    bt.grid(row=ligne, colomn = colonne)

    colonne += 1
    if colonne == 4:
        colonne = 0
        ligne += 1

bt = Label(fenetre,text = "Effacer",bg = "#476C9B",fg= "#FFF",height = 4, width =6)

#test commit1

