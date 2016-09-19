# Funciones extras para el sistema de muestras


def sanMuestras(texto):
    ''' recibe el texto de el area de muestras y devuelve una lista de
    las muestras encontradas.
     Importante notar que el escanner de barras lo configure para que separara los codigos con {--}
     si se cambia despues, hay que modificar esta funcion'''
    muestras = []
    texto = texto.strip()
    listaTexto = texto.split('--') #Esto es por que el escaner de barras esta configurado asi
    for a in listaTexto:
        if len(a) < 1: continue
        muestras.append(a.strip()) #quitamos los espacios y enters alrededor y lo agregamos a la lista
    muestras = list(set(muestras)) #Borramos los duplicados

    return muestras
