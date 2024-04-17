lista = [51,18,89,65,4,2,3,5,96,85,74,14,25,36,32,65,98,87,45,12]
stop= True
ordenar_numeros=[]
lista_temporal=lista.copy()
while stop:
  val_max=lista_temporal[0]
  for i in range(len(lista_temporal)):
     x=lista_temporal[i]

     if (x<val_max):
       val_max=x

  ordenar_numeros.append(val_max)
  lista_temporal.remove(val_max)
  if len(lista_temporal)==0:
     stop= False
print("lista ordenada",ordenar_numeros)
print("lista original",lista)
