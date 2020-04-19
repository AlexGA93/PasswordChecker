palabra = 'Patata'
countU = 0
countL = 0
countN = 0
for i in range(len(palabra)):
  if(i>0):
    #que es?
    if(palabra[i].isupper() and palabra[i-1].isupper()):
        #if(palabra[i-1].isupper()):
        countU+=1
    elif(palabra[i].islower() and palabra[i-1].islower()):
        #if(palabra[i-1].islower()):
        countL+=1
    elif(palabra[i].isnumeric() and palabra[i-1].isnumeric()):
        #if(palabra[i-1].isnumeric()):
        countN+=1

    

print(
  'Contador de Mayusculas consecutivas: ',countU,
  '\nContador de minusculas consecutivas: ',countL,
  '\nContador de Numros consecutivos: ',countN
)