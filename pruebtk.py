ventas = Tk()
ventas.title("LOCAL")
ventas.geometry("1000x1000")
ventas.resizable(False,False)
ventas.config(bg="black")

def saludar(nombre):
    print("Hola", nombre)

#creamos un boton centrado en la ventana
# boton = Button(ventas, text="Enviar", width=10, height=2, bg="white", fg="black", font=("Arial", 12), command=lambda: saludar("alex"))
# boton.place(x=200, y=200)

# cajatxt = Entry(ventas, width=30, font=("Arial", 12))
# cajatxt.place(x=150, y=150)

# boton1 = Button(ventas, text="b1",width=30)
# boton2 = Button(ventas, text="b2",width=30)
# boton3 = Button(ventas, text="b3",width=30)

# boton1.grid(row=0, column=0)
# boton2.grid(row=0, column=1)
# boton3.grid(row=0, column=2)

#creamos el loop de la ventana
ventas.mainloop()
