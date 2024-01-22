from tkinter import *

expression = ""
def appuyer(touche):
    if touche == "=":
        calculer()
        return
    global expression
    expression += str(touche)
    equation.set(expression)


def calculer():
    try:
        global expression
        total = str(eval(expression)) #fonction eval() = calcul tout
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def effacer():
    global expression
    expression = ""
    equation.set("")


fenetre = Tk()
fenetre.configure(background="#101419")
fenetre.title("Calculatrice de Noah")
fenetre.geometry("435x685")


equation = StringVar() #variable qui va stocker
resulat = Label(fenetre,bg="#101419",fg="#FFF",textvariable = equation, height= "4")
resulat.grid(columnspan=4)

#BOUTONS
boutons = [7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","="]
ligne = 1
colonne = 0
for button in boutons:
    bt = Label(fenetre,text = str(button),bg = "#476C9B",fg= "#FFF",height = 8, width =12)
    bt.bind("<Button-1>", lambda e, button=button: appuyer(button)) #rendre le texte cliquable
    bt.grid(row=ligne, column = colonne)

    colonne += 1
    if colonne == 4:
        colonne = 0
        ligne += 1

bt = Label(fenetre,text = "Effacer",bg = "#984447",fg= "#FFF",height = 4, width =26)
bt.bind("<Button-1>", lambda e: effacer())
bt.grid(columnspan=4)

fenetre.mainloop()




