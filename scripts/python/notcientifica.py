def convertir_a_notacion_cientifica(numero):
    # Usamos formato de notación científica para obtener la mantisa y el exponente
    notacion_cientifica = "{:.10e}".format(numero)
    
    # Dividimos la mantisa y el exponente
    mantisa, exponente = notacion_cientifica.split("e")
    exponente = int(exponente)  # Convertimos el exponente a un entero
    
    # Formateamos la salida en el formato solicitado
    resultado = f"{mantisa} \\cdot 10^{{{exponente}}}"
    return resultado

while True:
    numero = float(input("Ingresa un número: "))
    print("Notación científica:", convertir_a_notacion_cientifica(numero))