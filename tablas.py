#pedir al usuario por el número de tabla
print("dime el número de la tabla multiplicar")
num_tabla=int(input())
indice=1
while(indice < 11):
  resultado = num_tabla * indice
  print(indice , "x" , num_tabla , "=" , resultado)
  indice=indice + 1
  print("fin")