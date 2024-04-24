mensaje_tesoro= 2
mensaje_criatura= 3
mensaje_trampa= 5
mensaje_encontrado= input("ingrese la cantidad de circulos tallados en la estatua:")
mensaje_encontrado= int(mensaje_encontrado)

if mensaje_encontrado == mensaje_tesoro:
  print("has encontrado un tesoro!")

if mensaje_encontrado == mensaje_criatura:
  print("has encontrado una criatura magica!")

if mensaje_encontrado == mensaje_trampa:
  print("te has topado con una trampa mortal!")
else:
  print("la estatua no tiene nada de especial y no te has topado con nada")
