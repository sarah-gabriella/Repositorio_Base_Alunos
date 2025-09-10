peso=float(input(" peso"))

altura=float(input( " altura"))

imc=peso/(altura**2)
 
if imc<18.5:
  print("CLASSIFICAÇÃO ABAIXO DO PESO")

elif imc==24.9:
   print("CLASSIFICAÇÃO PESO NORMAL")
   
elif imc >=29.9:
   print("CLASSIFICAÇÃO SOBREPESO")
   
elif imc>30:
   print("CLASSIFIÇÃO ABAIXO DO PESO")
         
    