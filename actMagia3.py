equipo_magico= input("ingresar equipo magico:")
equipo_magico= int(equipo_magico)
hechiceros= input("ingresar cantidas de jugadores:")
hechiceros= int(hechiceros)

def calcular_factoriales(hechiceros):
  if hechiceros== 0 or hechiceros==1:
    return 1
  else:
    return hechiceros * calcular_factoriales(hechiceros - 1)

def calcular_combinaciones(hehiceros, equipo_magico):
  if hechiceros > equipo_magico:
    return 0
  else:
    return calcular_factoriales(hechiceros)//(calcular_factoriales(equipo_magico)*calcular_factoriales(hechiceros - equipo_magico))


print("la cantidad de combinacione de equipo:", equipo_magico)
