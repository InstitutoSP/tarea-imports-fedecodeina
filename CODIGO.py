import FUNCIONES as fc

while True:

  print("hola, seleccione una opcion")
  print("ingrese A para sumar")
  print("ingrese B para multiplicar")
  print("ingrese C para restar")
  print("ingrese D para dividir")
  operacion=input("elija la opcion: ")

  f= int(input("ingrese un numero: "))
  g= int(input("ingrese un numero: "))

  if operacion=="A":
    fc.sumar(f,g)

  elif operacion=="B":
    fc.multiplicar(f,g)

  elif operacion=="C":
    fc.restar(f,g)

  elif operacion=="D":
    fc.dividir(f,g)

  else:
    print("terminado")
    break



