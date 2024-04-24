potencia_hechizo= input("ingresa la potencia de tu hechizo:")
potencia_hechizo= int(potencia_hechizo)
defensa_enemigo= input("ingresa la defensa del enemigo:")
defensa_enemigo= int(defensa_enemigo)


if potencia_hechizo > defensa_enemigo:
  print("has derrotado al enemigo")
else:
    print("has perdido")
