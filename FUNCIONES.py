#FUNCIONES CALCULADORA :)


def sumar (a,b):
    resultado=a+b
    print(resultado)
def multiplicar (a,b):
  resultado=a*b
  print(resultado)
def restar (a,b):
  resultado=a-b
  print(resultado)
def dividir (a,b):
  resultado=a/b
  print(resultado)
  
#funciones lista 1 
def lista_ordenada_nombres_1(lista):
  stop= True
  ordenar_numeros=[]
  lista_temporal=lista.copy()
  while stop:
    val_max=lista_temporal[0]
    for i in range(len(lista_temporal)):
      x=lista_temporal[i]

      if (x>val_max):
        val_max=x

    ordenar_numeros.append(val_max)
    lista_temporal.remove(val_max)
    if len(lista_temporal)==0:
      stop= False
  return ordenar_numeros

  
  #funciones lista 2 
  
  
  #funciones lista nombres 