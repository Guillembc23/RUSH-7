import tkinter as tk

def jugador_manual(mano,control1,control2,extra1,extra2,nombre1,nombre2,enjoc,n_enjoc):
    cartas_jugadas = ['  ' for _ in range(5)]
    carta_seleccionada = None

    def seleccionar_carta(carta):
        global carta_seleccionada
        carta_seleccionada = carta

    def jugar_carta(indice_espacio):
        global carta_seleccionada
        if carta_seleccionada and cartas_jugadas[indice_espacio] == '  ':
            cartas_jugadas[indice_espacio] = carta_seleccionada
            actualizar_espacios()
            mano.remove(carta_seleccionada)
            carta_seleccionada = None
            actualizar_mano()
        elif cartas_jugadas[indice_espacio] != '  ':
            mano.append(cartas_jugadas[indice_espacio])
            actualizar_mano()
            if carta_seleccionada:
                cartas_jugadas[indice_espacio] = carta_seleccionada
                mano.remove(carta_seleccionada)
                carta_seleccionada = None
                actualizar_mano()
            else:
                cartas_jugadas[indice_espacio] = '  '
            actualizar_espacios()

    def confirmar_jugada():
        ventana.destroy()

    def actualizar_espacios():
        for i in range(0,5):
            etiquetas_espacios[i].config(text=cartas_jugadas[i])

    def actualizar_mano():
        for widget in frame_mano.winfo_children():
            widget.destroy()

        for carta in mano:
            boton = tk.Button(frame_mano, text=carta, width=4, command=lambda c=carta: seleccionar_carta(c))
            boton.pack(side=tk.LEFT, padx=5)
            botones_mano.append(boton)

    def arreglat(control):
        res = "["
        for j in range(0,4):
            res += control[j] + " "
        return res + "]"

    ventana = tk.Tk()
    ventana.title("RUSH 7")
    frame_espacios = tk.Frame(ventana)
    frame_espacios.pack(pady=10)
    etiquetas_espacios = []

    for i in range(5):
        etiqueta = tk.Label(frame_espacios, text=f"{arreglat(control2[i])}", width=20, anchor="w")
        etiqueta.grid(row=0, column=i, padx=5, pady=5)
    for i in range(5):
        etiqueta = tk.Label(frame_espacios, text=f"{arreglat(control1[i])}", width=20, anchor="w")
        etiqueta.grid(row=1, column=i, padx=5, pady=5)
    for i in range(5):
        etiqueta = tk.Label(frame_espacios, text=f"", width=5, anchor="e")
        etiqueta.grid(row=2, column=i, padx=5, pady=5)
        etiquetas_espacios.append(etiqueta)
    for i in range(5):
        boton_jugar = tk.Button(frame_espacios, text="Jugar / Retirar Carta", command=lambda idx=i: jugar_carta(idx))
        boton_jugar.grid(row=3, column=i, padx=5, pady=5)


    frame_mano = tk.Frame(ventana)
    frame_mano.pack(pady=10)
    botones_mano = []
    actualizar_mano()

    boton_confirmar = tk.Button(ventana, text="Confirmar Jugada", command=confirmar_jugada)
    boton_confirmar.pack(pady=10)

    ventana.mainloop()
    juga = [cartas_jugadas[i] for i in range(0,5) if cartas_jugadas[i] != '  ']
    return mano, juga

