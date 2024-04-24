equipo= input("ingresar equipo:")
equipo= int(equipo)
personas= input("ingresar cantidas de personas:")
personas= int(personas)

def calcular_factoriales(personas):
  if personas== 0 or personas==1:
    return 1
  else:
    return personas * calcular_factoriales(personas - 1)

def calcular_combinaciones(peronas, equipo):
  if personas > equipo:
    return 0
  else:
    return calcular_factoriales(personas)//(calcular_factoriales(equipo)*calcular_factoriales(personas - equipo))
