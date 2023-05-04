from fileinput import filename
import json
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from turtle import fd
from grafosCaminosSimple import RandomGraph

import subprocess


class Menu_Inicio():
    
    def __init__(self):
        self.ven1 = Tk()
        self.ven1.title("PROYECTO MC2 GRAFOS")
        self.ven1.configure(background='black')
        # definir tamaño de ventana
        #self.ven1.geometry('500x600')
        #self.ven1.resizable(width=0, height=0)
        #self.ven1.geometry()
        
        self.Menu_Principal()



        
    def CrearCamino_Optimo(self):
        inicio=self.entradaVinicioVinicio.get()
        final=self.entradaVerticesFinal.get()
        if inicio and final :
            Inicio = inicio
            Final = final
        else:
            # manejar el caso cuando el valor de entrada está vacío
            print('ingrese las letras')

        self.objeto.draw_path(Inicio,Final)


        

    def CrearGrafo(self):
        numero1=self.entradaVertices.get()
        numero2=self.entradaAristas.get()
        print(numero1,numero2)
        try:
            verticeNumero = int(numero1)
            aristaNumero = int(numero2)
        except ValueError:
            # manejar el caso cuando el valor de entrada no es un entero válido
            print('no se a ingresado nada')
        
        self.objeto = RandomGraph(verticeNumero,aristaNumero)
        self.objeto.show_graph()

    def Menu_Principal(self):
        self.Frame = Frame(height=600, width=800)
        self.Frame.configure(background="black")
        
        
        self.text=""
        self.entradaVertices = tkinter.Entry(self.Frame)
        self.entradaVertices.grid(row=75 , column=50)
        numero1 = self.entradaVertices.get()
        

        self.entradaAristas = tkinter.Entry(self.Frame)
        self.entradaAristas.grid(row=100, column=50)
        numero2 = self.entradaAristas.get()
        #arista = self.NumeroEntero(numero2)

        

        self.entradaVinicioVinicio = tkinter.Entry(self.Frame)
        self.entradaVinicioVinicio.grid(row=150, column=50)
        

        self.entradaVerticesFinal = tkinter.Entry(self.Frame)
        self.entradaVerticesFinal.grid(row=200 , column=50)
        

        self.etiqueta = tkinter.Label(self.Frame, text="Ingrese Numero de vertic:")
        self.etiqueta.grid(row=75, column=0)
        self.etiqueta2 = tkinter.Label(self.Frame, text="Ingrese Numero de Aristas:")
        self.etiqueta2.grid(row=100, column=0)

        self.etiqueta3 = tkinter.Label(self.Frame, text="Ingrese posicion inicial:")
        self.etiqueta3.grid(row=150, column=0)

        self.etiqueta3 = tkinter.Label(self.Frame, text="Ingrese posicion Final:")
        self.etiqueta3.grid(row=200, column=0)
        

        
        
        
        self.buton1=Button(self.Frame, text="Generar Grafo",width=0, anchor="c",command=self.CrearGrafo,background="darkorange", font=("Arial", 12))
        self.buton1.grid(row=300, column=50)
        self.buton2=Button(self.Frame, text="Camino Optimo", width=0, anchor="c",command=self.CrearCamino_Optimo,background="darkorange", font=("Arial", 12))
        self.buton2.grid(row=300, column=75)
        self.Frame.pack()
        
        self.Frame.mainloop()

r = Menu_Inicio()