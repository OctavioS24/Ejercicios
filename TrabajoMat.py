from tkinter import *


def V2():

    def V3():

        def V4():# Botones de Mayor y Menor

            def V5():

                def V6():

                    def V7():

                        def V8():

                            def V9():
                                V8.withdraw()
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

                            # V7.withdraw()
                            # #Win = Toplevel()
                            # V8 = Tk()
                            # V8.geometry("600x200")
                            # V8.title("Ventana Español")
                            # V8.config(bg="orange")
                            # V8.resizable(width = False, height = False)

                            # L9 =  Label(V8, text= " Pensaste el Numero: ", font = "Bahnschrift 20" , background = "black",foreground = "white")
                            # L9.place(x= 180, y= 40)

                            # E7 = Entry(V8, background = "black", foreground = "white")
                            # E7.place(x= 220, y= 90, width = 200, height = 40)

                            # B6 = Button(V8, text = "  SALIR  ", width = 15 , background = "Yellow", command = V9)
                            # B6.place(x= 260, y= 140)

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

                        V6.withdraw()
                        #Win = Toplevel()
                        V7 = Tk()
                        V7.geometry("600x200")
                        V7.title("Ventana Español")
                        V7.config(bg="orange")
                        V7.resizable(width = False, height = False)

                        L8 =  Label(V7, text= "Pensaste el Numero: ", font = "Bahnschrift 20" , background = "black",foreground = "white")
                        L8.place(x= 180, y= 40)

                        E6 = Entry(V7, background = "black", foreground = "white", state="readonly")
                        E6.place(x= 220, y= 90, width = 200, height = 40)

                        B6 = Button(V7, text = "  SALIR  ", width = 15 , background = "Yellow", command= V7.destroy)
                        B6.place(x= 260, y= 140)

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

                    V5.withdraw()
                    #Win = Toplevel()
                    V6 = Tk()
                    V6.geometry("600x200")
                    V6.title("Ventana Español")
                    V6.config(bg="orange")
                    V6.resizable(width = False, height = False)

                    L7 = Label(V6, text= "5)Ahora sumá las cifras del número que pensaste al principio", font = "Bahnschrift 16" , background = "black",foreground = "white")
                    L7.place(x= 3, y= 40)

                    E5 = Entry(V6, background = "black", foreground = "white")
                    E5.place(x= 220, y= 90, width = 200, height = 40)

                    B6 = Button(V6, text = "SIGUIENTE", width = 15 , background = "Yellow", command= V7)
                    B6.place(x= 260, y= 140)

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

                V4.withdraw()
                #Win = Toplevel()
                V5 = Tk()
                V5.geometry("600x200")
                V5.title("Ventana Español")
                V5.config(bg="orange")
                V5.resizable(width = False, height = False)

                L6 = Label(V5, text= "4) Entonces, restá el número que pensaste del nuevo número", font = "Bahnschrift 16" , background = "black",foreground = "white")
                L6.place(x= 3, y= 40)

                E4 = Entry(V5, background = "black", foreground = "white")
                E4.place(x= 220, y= 90, width = 200, height = 40)

                B5 = Button(V5, text = "SIGUIENTE", width = 15 , background = "Yellow", command= V6)
                B5.place(x= 260, y= 140)

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
            

            def Funcion():
                op = oper.get()
                if op == 1:
                    pass
                if op == 2:
                    pass
            
            V3.withdraw()   
            #Win = Toplevel()
            V4 = Tk()
            V4.geometry("600x200")
            V4.title("Ventana Español")
            V4.config(bg="orange")
            V4.resizable(width = False, height = False)
            oper= IntVar()

            L5=  Label(V4, text= "3)¿El nuevo número es mayor o menor que el primero?", font="Bahnschrift 18" , background = "black",foreground = "white")
            L5.place(x= 3, y= 40)

            #E3 = Entry(V4, background = "black", foreground = "white")
            #E3.place(x=220, y= 90, width = 200, height = 40)

            Mayor = Button(V4, text = "MAYOR", width = 15 , height= 2, font="Areal 12", background = "Yellow", value = 1, variable = oper, command= Funcion)
            Mayor.place(x= 200, y= 90)

            Menor = Button(V4, text = "MENOR", width = 15 , height= 2, font="Areal 12", background = "Yellow",value = 2, variable = oper, command= Funcion)
            Menor.place(x= 200, y= 150)

            Siguiente = Button(V4, text="SIGUIENTE", height= 1, font="Areal 12", background = "Yellow", command = V5)
            Siguiente.place(x= 380, y= 130)

            

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

        V2.withdraw()
        #Win = Toplevel()
        V3 = Tk()
        V3.geometry("600x200")
        V3.title("Ventana Español")
        V3.config(bg="orange")
        V3.resizable(width = False, height = False)

        L4 = Label(V3, text = "2) Invertí el orden de las cifras", font="Bahnschrift 18" , background = "black",foreground = "white")
        L4.place(x= 130, y= 30)

        #E2 = Entry(V3, background = "black", foreground = "white")
        #E2.place(x = 220, y = 80, width = 200, height = 40)

        B3 = Button(V3, text = "SIGUIENTE", width = 15, height= 2, font="Areal 12", background = "Yellow", command= V4)
        B3.place(x=220, y=130)

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

    op = oper.get()
    if op == 1:
        V1.withdraw()
        #Win = Toplevel()
        V2 = Tk()
        V2.geometry("600x200")
        V2.title("Ventana Español")
        V2.config(bg="orange")
        V2.resizable(width = False, height = False)

        L3 = Label(V2, text= "1) Pensá un número de dos cifras (que no sean iguales)", font="Bahnschrift 18" , background = "black",foreground="white")
        L3.place(x= 5, y= 40)

        #E1 = Entry(V2, background = "black", foreground = "white")
        #E1.place(x=190, y= 100, width = 200, height = 40)

        B2 = Button(V2, text="SIGUIENTE",width = 20, height= 2 , font="Areal 12", background = "Yellow", command= V3)
        B2.place(x=200, y=130)
        

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

    '''if op == 2:
        Ventana.withdraw()
        #Win = Toplevel()
        Win = Tk()
        Win.geometry("600x400")
        Win.title("Ventana Ingles")
        Win.config(bg="Gray")

        L3 = Label(Win, text= "1) Think of a two-digit number (that are not the same)")
        L3.place(x= 70, y= 40)

        E1 = Entry(Win)
        E1.place(x=370, y= 40)

        L4 = Label(Win, text= "2) I reversed the order of the numbers")
        L4.place(x= 70, y= 80)

        E2 = Entry(Win)
        E2.place(x=280, y= 80)

        L5=  Label(Win, text= "3) Is the new number greater or less than the first?")
        L5.place(x= 70, y= 120)

        E3 = Entry(Win)
        E3.place(x=360, y= 120)

        L6 = Label(Win, text= "4) So, subtract the number you thought of from the new number")
        L6.place(x= 70, y= 160)

        E4 = Entry(Win)
        E4.place(x= 420, y= 160)

        L7 = Label(Win, text= "5) Now add the digits of the number you thought of at first")
        L7.place(x= 70, y= 200)

        E5 = Entry(Win)
        E5.place(x= 400, y= 200)

        L8 =  Label(Win, text= "6) Tell me the numbers you got")
        L8.place(x= 70, y= 240)

        E6 = Entry(Win)
        E6.place(x= 280, y= 240)

        E7 = Entry(Win)
        E7.place(x= 430, y= 240)

        L9 =  Label(Win, text= "Did you think the Number: ")
        L9.place(x= 70, y= 280)

        E8 = Entry(Win)
        E8.place(x= 230, y= 280)'''

V1=Tk()
V1.geometry("600x400")
V1.title("Adivina Adivinador")
V1.config(bg="orange")
V1.resizable(width = False, height = False)
oper = IntVar()


L1 = Label(V1, text = "Juego Adivina Adivinador", font="Algerian 28", background = "Yellow" )
L1.place( x= 60, y = 50)

L2 = Label(V1, text = "   Elije un idioma   ", font="Bahnschrift 20" , background = "black",foreground="white")
L2.place( x= 190, y = 130)

RB1 = Radiobutton(V1, text = "ESPAÑOL", font="Bahnschrift 12", background = "black",foreground="white", value = 1, variable = oper)
RB1.place(x= 150, y= 220)

RB2 = Radiobutton(V1, text = " INGLES ", font="Bahnschrift 12", background = "black",foreground="white", value = 2, variable = oper)
RB2.place(x= 380, y= 220)

B1 = Button(V1, text = "ACEPTAR", font = "Bahnschrift 12", background="Yellow", command = V2)
B1.place(x= 270, y= 280)

V1.mainloop()